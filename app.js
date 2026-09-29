const formatPrice = (price) => {
  const value = Number(price);
  if (!Number.isFinite(value)) return price || "สอบถามราคา";
  return new Intl.NumberFormat("th-TH", {
    style: "currency",
    currency: "THB",
    maximumFractionDigits: 0,
  }).format(value);
};

const displayProperties = (properties) => {
  const list = document.querySelector("#property-list");
  const count = document.querySelector("#listing-count");
  count.textContent = `${properties.length} รายการ`;

  if (!properties.length) {
    list.innerHTML = '<p class="empty">ยังไม่มีประกาศในขณะนี้</p>';
    return;
  }

  const template = document.querySelector("#property-template");
  properties.forEach((property) => {
    const item = template.content.cloneNode(true);
    const image = item.querySelector(".property-image");
    image.src = property.image || "images/property-placeholder.svg";
    image.alt = property.title || "รูปภาพอสังหาริมทรัพย์";
    item.querySelector(".property-location").textContent = property.location || "";
    item.querySelector(".property-title").textContent = property.title || "ประกาศบ้านและที่ดิน";
    item.querySelector(".property-price").textContent = formatPrice(property.price);
    item.querySelector(".property-description").textContent = property.description || "";

    const facts = [
      ["ห้องนอน", property.bedrooms],
      ["ห้องน้ำ", property.bathrooms],
      ["พื้นที่", property.area],
    ].filter(([, value]) => value);
    item.querySelector(".property-facts").innerHTML = facts
      .map(([label, value]) => `<div><dt>${label}</dt><dd>${value}</dd></div>`)
      .join("");
    list.appendChild(item);
  });
};

fetch("data/properties.json")
  .then((response) => response.json())
  .then((data) => displayProperties(data.properties || []))
  .catch(() => displayProperties([]));
