/* Andaman Land — progressive enhancement only.
   All property content is rendered in the HTML; this script filters what is already there. */
(function () {
  "use strict";

  /* ---------------- mobile nav ---------------- */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  /* ---------------- remember language choice ---------------- */
  try {
    var htmlLang = document.documentElement.getAttribute("data-lang");
    if (htmlLang) localStorage.setItem("al_lang", htmlLang);
  } catch (e) { /* storage unavailable — ignore */ }

  /* ---------------- listing filters ---------------- */
  var list = document.getElementById("listing-grid");
  if (list) {
    var cards = Array.prototype.slice.call(list.querySelectorAll("[data-card]"));
    var countEl = document.getElementById("result-count");
    var emptyEl = document.getElementById("result-empty");
    var form = document.getElementById("filter-form");
    var sortEl = document.getElementById("sort-select");

    var bands = {
      price: { "0-10": [0, 1e7], "10-30": [1e7, 3e7], "30-60": [3e7, 6e7], "60-100": [6e7, 1e8], "100+": [1e8, 1e12] },
      size: { "0-1": [0, 1], "1-3": [1, 3], "3-10": [3, 10], "10-50": [10, 50], "50+": [50, 1e6] }
    };

    function val(name) {
      var el = form ? form.querySelector('[name="' + name + '"]') : null;
      return el ? el.value : "";
    }

    function inBand(raw, band, table) {
      if (!band) return true;
      if (raw === "" || raw === null || isNaN(parseFloat(raw))) return false; // unknown value
      var range = table[band];
      if (!range) return true;
      var n = parseFloat(raw);
      return n >= range[0] && n < range[1];
    }

    function apply() {
      var loc = val("location"), type = val("type"), price = val("price"), size = val("size");
      var shown = 0;
      cards.forEach(function (card) {
        var ok = (!loc || card.dataset.loc === loc) &&
                 (!type || card.dataset.type === type) &&
                 inBand(card.dataset.price, price, bands.price) &&
                 inBand(card.dataset.size, size, bands.size);
        card.hidden = !ok;
        if (ok) shown++;
      });
      if (countEl) countEl.textContent = String(shown);
      if (emptyEl) emptyEl.hidden = shown !== 0;
      sort();
    }

    function num(v, fallback) {
      var n = parseFloat(v);
      return isNaN(n) ? fallback : n;
    }

    function sort() {
      if (!sortEl) return;
      var mode = sortEl.value;
      var visible = cards.filter(function (c) { return !c.hidden; });
      visible.sort(function (a, b) {
        if (mode === "price-asc") return num(a.dataset.price, Infinity) - num(b.dataset.price, Infinity);
        if (mode === "price-desc") return num(b.dataset.price, -Infinity) - num(a.dataset.price, -Infinity);
        if (mode === "size") return num(b.dataset.size, -Infinity) - num(a.dataset.size, -Infinity);
        return (b.dataset.created || "").localeCompare(a.dataset.created || "");
      });
      visible.forEach(function (c) { list.appendChild(c); });
    }

    // read filters from the URL so the home-page search box works
    var params = new URLSearchParams(window.location.search);
    ["location", "type", "price", "size"].forEach(function (key) {
      var v = params.get(key);
      if (!v || !form) return;
      var el = form.querySelector('[name="' + key + '"]');
      if (el) el.value = v;
    });

    if (form) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var q = new URLSearchParams();
        ["location", "type", "price", "size"].forEach(function (k) { if (val(k)) q.set(k, val(k)); });
        var url = window.location.pathname + (q.toString() ? "?" + q.toString() : "");
        if (window.history && history.replaceState) history.replaceState(null, "", url);
        apply();
      });
      form.addEventListener("change", apply);
      var reset = document.getElementById("filter-reset");
      if (reset) reset.addEventListener("click", function () {
        form.reset();
        if (window.history && history.replaceState) history.replaceState(null, "", window.location.pathname);
        apply();
      });
    }
    if (sortEl) sortEl.addEventListener("change", sort);
    apply();
  }

  /* ---------------- enquiry forms ---------------- */
  function encode(data) {
    return Object.keys(data).map(function (k) {
      return encodeURIComponent(k) + "=" + encodeURIComponent(data[k]);
    }).join("&");
  }

  Array.prototype.forEach.call(document.querySelectorAll("form[data-enquiry]"), function (form) {
    var status = form.querySelector(".form-status");
    var submit = form.querySelector('[type="submit"]');
    var msgs = JSON.parse(form.getAttribute("data-messages") || "{}");

    function setError(field, text) {
      var slot = form.querySelector('[data-err="' + field + '"]');
      if (slot) slot.textContent = text || "";
      var input = form.querySelector('[name="' + field + '"]');
      if (input) input.setAttribute("aria-invalid", text ? "true" : "false");
    }

    function show(kind, text) {
      if (!status) return;
      status.textContent = text;
      status.className = "form-status show " + kind;
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var data = {};
      Array.prototype.forEach.call(form.elements, function (el) {
        if (el.name && el.type !== "submit") data[el.name] = (el.value || "").trim();
      });

      if (data["company-website"]) return; // honeypot: silently drop bots

      var ok = true;
      ["name", "email", "message", "contact"].forEach(function (f) { setError(f, ""); });
      if (!data.name) { setError("name", msgs.name || "Required"); ok = false; }
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(data.email || "")) { setError("email", msgs.email || "Invalid email"); ok = false; }
      if (!data.phone && !data.whatsapp && !data.line) { setError("contact", msgs.contact || "Add a contact method"); ok = false; }
      if (!data.message || data.message.length < 5) { setError("message", msgs.message || "Required"); ok = false; }
      if (!ok) { show("bad", msgs.fail_validate || ""); if (status && !msgs.fail_validate) status.className = "form-status"; return; }

      try {
        var last = parseInt(sessionStorage.getItem("al_last_send") || "0", 10);
        if (Date.now() - last < 60000) { show("bad", msgs.wait || "Please wait"); return; }
      } catch (err) { /* ignore */ }

      var endpoint = form.getAttribute("data-endpoint") || "";
      if (submit) { submit.disabled = true; submit.dataset.label = submit.textContent; submit.textContent = msgs.sending || "Sending…"; }

      var request = endpoint
        ? fetch(endpoint, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(data) })
        : fetch("/", { method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" }, body: encode(Object.assign({ "form-name": form.getAttribute("name") }, data)) });

      request.then(function (res) {
        if (!res.ok) throw new Error("bad status");
        try { sessionStorage.setItem("al_last_send", String(Date.now())); } catch (err) {}
        form.reset();
        show("ok", msgs.ok || "Sent");
      }).catch(function () {
        show("bad", msgs.fail || "Could not send");
      }).then(function () {
        if (submit) { submit.disabled = false; submit.textContent = submit.dataset.label || "Send"; }
      });
    });
  });
})();
