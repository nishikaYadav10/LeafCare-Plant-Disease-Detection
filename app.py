<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>LeafCare | Plant Health Assistant</title>

<style>
:root {
  --green: #13865b;
  --light: #e9f7ef;
  --bg: #f5f9f6;
  --card: #ffffff;
  --text: #20352a;
  --muted: #687b70;
  --border: #dce9e0;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background: var(--bg);
  color: var(--text);
}
button, input { font: inherit; }
button { cursor: pointer; }
.app { display: flex; min-height: 100vh; }
.sidebar {
  width: 245px;
  background: var(--card);
  border-right: 1px solid var(--border);
  padding: 25px 16px;
  flex-shrink: 0;
}
.brand { font-size: 25px; font-weight: bold; color: var(--green); }
.brand small { display: block; font-size: 12px; color: var(--muted); margin-top: 6px; }
nav { margin-top: 35px; display: grid; gap: 8px; }
nav button {
  text-align: left; padding: 14px; border: 0; border-radius: 10px;
  background: transparent; color: var(--muted); font-weight: bold;
}
nav button.active, nav button:hover { background: var(--light); color: var(--green); }
.sidebar-note {
  margin-top: 40px; padding: 14px; background: var(--light);
  border-radius: 12px; font-size: 13px; line-height: 1.6;
}
.main { flex: 1; min-width: 0; }
header {
  display: flex; justify-content: space-between; align-items: center;
  gap: 12px; padding: 18px 30px; background: var(--card);
  border-bottom: 1px solid var(--border);
}
header button, .secondary {
  border: 1px solid var(--border); background: var(--card);
  color: var(--text); padding: 10px 14px; border-radius: 9px;
}
.content { max-width: 1150px; margin: auto; padding: 30px; }
.page { display: none; }
.page.active { display: block; }
h1 { font-size: clamp(27px, 4vw, 38px); margin: 10px 0; }
h2 { margin-top: 25px; }
p { line-height: 1.6; }
.muted { color: var(--muted); }
.green { color: var(--green); }
.panel {
  background: var(--card); border: 1px solid var(--border);
  border-radius: 18px; padding: 23px; margin: 18px 0;
}
.grid {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
  gap: 16px;
}
.stat { background: var(--card); padding: 20px; border-radius: 15px; border: 1px solid var(--border); }
.stat strong { display: block; color: var(--green); font-size: 27px; margin-bottom: 6px; }
.primary {
  border: 0; border-radius: 10px; background: var(--green); color: white;
  padding: 12px 18px; font-weight: bold;
}
.primary:hover { background: #0b6844; }
.upload {
  border: 2px dashed #9acbb0; border-radius: 15px; padding: 28px;
  text-align: center; background: var(--light);
}
.upload input { display: block; max-width: 100%; margin: 18px auto; }
#preview { max-width: 100%; max-height: 280px; border-radius: 12px; margin: 12px auto; }
#resultImage { width: 100%; max-height: 280px; object-fit: contain; border-radius: 12px; }
input[type="search"] {
  width: 100%; padding: 14px; border: 1px solid var(--border);
  border-radius: 10px; margin: 12px 0; background: var(--card); color: var(--text);
}
.filters { display: flex; gap: 8px; flex-wrap: wrap; margin: 12px 0 20px; }
.filter {
  padding: 9px 16px; border: 1px solid var(--border);
  border-radius: 30px; background: var(--card); color: var(--text);
}
.filter.active { background: var(--green); color: white; }
.disease-card {
  border: 1px solid var(--border); border-radius: 15px;
  padding: 18px; background: var(--card);
}
.disease-card h3 { margin-top: 5px; }
.disease-card p { font-size: 14px; color: var(--muted); }
.disease-card button { margin-top: 8px; }
details {
  background: var(--card); border: 1px solid var(--border);
  border-radius: 12px; margin: 12px 0; padding: 15px;
}
summary { cursor: pointer; font-weight: bold; color: var(--green); }
details p, details li { line-height: 1.7; }
.notice {
  padding: 13px; border-radius: 10px; background: #fff6dd;
  color: #70551a; font-size: 13px; line-height: 1.6; margin-top: 18px;
}
footer { text-align: center; color: var(--muted); padding: 24px; font-size: 13px; }
.hidden { display: none !important; }
body.dark {
  --bg: #101a14; --card: #18271e; --text: #edf6ef;
  --muted: #b0c1b5; --border: #304438; --light: #203a2b;
}
@media(max-width:760px) {
  .app { display: block; }
  .sidebar { width: 100%; border-right: 0; border-bottom: 1px solid var(--border); padding: 15px; }
  nav { margin-top: 15px; grid-template-columns: repeat(2, 1fr); }
  nav button { padding: 10px; font-size: 13px; }
  .sidebar-note { display: none; }
  header { padding: 14px; }
  .content { padding: 17px; }
}
</style>
</head>

<body>
<div class="app">
  <aside class="sidebar">
    <div class="brand">🌿 LeafCare
      <small>Plant Health & Treatment Advisory</small>
    </div>

    <nav>
      <button class="active" data-page="dashboard">▦ Dashboard</button>
      <button data-page="analyze">📷 Analyze Plant</button>
      <button data-page="guide">📖 Disease & Treatment Guide</button>
      <button data-page="tips">🌱 Tips & Prevention</button>
    </nav>

    <div class="sidebar-note">
      <strong>🌱 Plant health matters</strong>
      <p>Upload a clear leaf photograph to check for a possible disease and explore care recommendations.</p>
      <p>Model: MobileNetV2 (planned integration)</p>
    </div>
  </aside>

  <div class="main">
    <header>
      <strong id="breadcrumb">Dashboard</strong>
      <div>
        <button id="themeButton">🌙 Theme</button>
        <button id="languageButton">हिंदी</button>
      </div>
    </header>

    <main class="content">

      <section class="page active" id="dashboard">
        <p class="green"><strong>WELCOME TO LEAFCARE 🌱</strong></p>
        <h1>Let's keep your plants healthy.</h1>
        <p class="muted">Explore plant diseases, upload leaf photographs, and learn about possible treatments.</p>

        <div class="panel">
          <h2>Check your plant</h2>
          <p>Choose a leaf photograph to begin.</p>
          <button class="primary" onclick="showPage('analyze')">＋ Analyze a Plant</button>
        </div>

        <div class="grid">
          <div class="stat"><strong>7</strong>Supported disease classes</div>
          <div class="stat"><strong>2</strong>Supported crops</div>
          <div class="stat"><strong id="scanCount">0</strong>Analyses attempted</div>
        </div>

        <div class="panel">
          <h2>How LeafCare works</h2>
          <ol>
            <li>Upload a clear photograph of a plant leaf.</li>
            <li>The connected AI model predicts a possible condition.</li>
            <li>Review the confidence score and advisory information.</li>
            <li>Follow appropriate prevention and care practices.</li>
          </ol>
          <p class="muted">The image prediction feature requires a running backend model. The guide and other frontend features can be explored without it.</p>
        </div>

        <div class="panel">
          <h2>Recent activity</h2>
          <ul id="history"><li class="muted">No analyses yet.</li></ul>
          <button class="secondary" id="clearHistory">Clear history</button>
        </div>
      </section>

      <section class="page" id="analyze">
        <h1>Analyze Plant</h1>
        <p class="muted">Upload a leaf photograph for analysis by your connected model.</p>

        <div class="panel">
          <div class="upload">
            <h2>🍃 Upload a leaf image</h2>
            <p>Use a clear photograph with one leaf in focus.</p>
            <input type="file" id="imageInput" accept="image/*">
            <img id="preview" class="hidden" alt="Selected leaf preview">
          </div>
          <p id="uploadMessage" class="muted">No image selected.</p>
          <button class="primary" id="analyzeButton">Analyze leaf</button>
        </div>

        <div class="panel hidden" id="resultPanel">
          <h2>Analysis result</h2>
          <img id="resultImage" alt="Analyzed leaf">
          <h3 id="resultDisease"></h3>
          <p id="resultConfidence"></p>
          <div id="resultAdvice"></div>
        </div>

        <div class="notice">
          The Analyze button sends the photo to the LeafCare model server (<code>/predict</code>).
          Predictions come from a MobileNetV2 model trained on potato and tomato leaves.
        </div>
      </section>

      <section class="page" id="guide">
        <h1>Disease & Treatment Guide</h1>
        <p class="muted">Explore the supported potato and tomato conditions, their symptoms, treatment options, and prevention.</p>

        <input id="searchInput" type="search" placeholder="Search by disease, crop, or symptom...">

        <div class="filters">
          <button class="filter active" data-crop="All">All crops</button>
          <button class="filter" data-crop="Potato">🥔 Potato</button>
          <button class="filter" data-crop="Tomato">🍅 Tomato</button>
        </div>

        <div class="grid" id="diseaseList"></div>
        <h2>Treatment & Prevention Details</h2>
        <div id="treatmentList"></div>

        <div class="notice">
          These are general educational recommendations, not a confirmed diagnosis.
          Before using pesticides or fungicides, verify the product, dosage, and safety precautions with a qualified local agriculture professional.
        </div>
      </section>

      <section class="page" id="tips">
        <h1>Tips & Prevention</h1>
        <p class="muted">Good practices can help reduce the risk of many plant diseases.</p>
        <div class="grid" id="tipsList"></div>
      </section>
    </main>

    <footer>LeafCare — Plant Disease Detection & Treatment Advisory System</footer>
  </div>
</div>

<script>
// Where the Flask server lives. Same address when Flask serves this page (laptop or Render).
// If the page is opened from VS Code Live Server (port 5500) or as a plain file, use the local Flask server.
const API_BASE = (location.protocol === "file:" || location.port === "5500") ? "http://127.0.0.1:5000" : "";

const diseases = [
  {
    crop:"Potato", name:"Early Blight", emoji:"🥔",
    symptoms:"Brown spots, often with concentric rings, on older leaves. Yellowing may appear around the spots.",
    about:"Early blight is a fungal disease associated with Alternaria species. Symptoms and severity can vary with weather and crop conditions.",
    treatment:["Remove badly affected leaves where practical and dispose of infected plant material appropriately.","Avoid wetting foliage when watering.","If the disease continues to spread, ask a local agriculture professional about an approved fungicide and its label instructions."],
    prevention:["Rotate crops where possible.","Maintain suitable spacing and airflow.","Avoid leaving infected plant debris around the crop."]
  },
  {
    crop:"Potato", name:"Late Blight", emoji:"🥔",
    symptoms:"Water-soaked-looking dark patches that can enlarge quickly, sometimes with pale growth near lesion edges in humid conditions.",
    about:"Late blight is a serious disease caused by Phytophthora infestans. It can spread rapidly in cool, wet conditions.",
    treatment:["Remove and dispose of affected plants according to local agricultural guidance.","Avoid moving infected plant material through the field.","Contact an agriculture officer promptly for locally approved disease-management advice."],
    prevention:["Inspect crops regularly, especially during wet weather.","Use healthy planting material and suitable resistant varieties where available.","Follow local disease alerts and recommended crop-protection guidance."]
  },
  {
    crop:"Potato", name:"Healthy", emoji:"🥔",
    symptoms:"Leaves generally have an even green colour and no obvious expanding lesions or unusual patterns.",
    about:"A healthy-looking leaf does not guarantee the entire plant is disease-free. Continue routine monitoring.",
    treatment:["No disease treatment is indicated by appearance alone.","Continue normal crop care and investigate any new symptoms."],
    prevention:["Provide appropriate sunlight and watering.","Maintain good soil drainage and nutrition.","Inspect both sides of leaves regularly."]
  },
  {
    crop:"Tomato", name:"Healthy", emoji:"🍅",
    symptoms:"Leaves generally show normal colour and growth without obvious disease lesions or abnormal patterns.",
    about:"Healthy-looking leaves are a positive sign, but regular plant monitoring is still important.",
    treatment:["No disease treatment is indicated by appearance alone.","Continue routine care and watch for changes."],
    prevention:["Water near the soil instead of repeatedly wetting leaves.","Provide suitable spacing and sunlight.","Check plants regularly for pests and symptoms."]
  },
  {
    crop:"Tomato", name:"Leaf Mold", emoji:"🍅",
    symptoms:"Yellowish patches on the upper leaf surface may occur with olive-green or brownish growth underneath in humid conditions.",
    about:"Tomato leaf mold is associated with the fungus Passalora fulva and is favoured by high humidity.",
    treatment:["Remove heavily affected leaves when practical.","Improve ventilation and avoid prolonged leaf wetness.","Ask a local agriculture professional about approved control products if the disease persists."],
    prevention:["Increase airflow between plants.","Use watering practices that keep foliage as dry as practical.","Manage greenhouse or growing-area humidity where possible."]
  },
  {
    crop:"Tomato", name:"Mosaic Virus", emoji:"🍅",
    symptoms:"Mottled light and dark green leaf patterns, distortion, or unusual leaf growth may occur.",
    about:"Mosaic-like symptoms can be associated with plant viruses, but visual symptoms alone cannot confirm which virus is present.",
    treatment:["There is generally no curative treatment for a plant once a viral infection is established.","Isolate suspicious plants where practical and seek local agricultural guidance.","Clean tools and handle plants carefully to reduce mechanical spread."],
    prevention:["Use healthy seeds and planting material.","Control relevant insect vectors when advised by local experts.","Clean tools and wash hands after handling suspicious plants."]
  },
  {
    crop:"Tomato", name:"Target Spot", emoji:"🍅",
    symptoms:"Circular brown leaf lesions may develop concentric rings, sometimes giving a target-like appearance.",
    about:"Target spot is associated with the fungus Corynespora cassiicola. Other conditions can produce similar spots.",
    treatment:["Remove severely affected foliage where practical.","Avoid overhead watering and improve airflow.","Seek local advice about approved fungicides if the disease is spreading."],
    prevention:["Inspect leaves regularly.","Avoid excessive foliage wetness.","Maintain suitable plant spacing and remove crop debris."]
  }
];

const tips = [
  ["💧","Water carefully","Water near the soil and avoid repeatedly wetting leaves, especially late in the day."],
  ["☀️","Provide suitable sunlight","Follow the light requirements of your crop and avoid overcrowding plants."],
  ["🔎","Inspect leaves regularly","Look at both sides of leaves and check for new spots, discolouration, or unusual growth."],
  ["🌬️","Improve airflow","Suitable spacing can help foliage dry faster and reduce conditions favourable to some diseases."],
  ["🧹","Keep the growing area clean","Remove diseased plant debris appropriately and clean tools between plants."],
  ["🌱","Use healthy planting material","Choose healthy seeds or seedlings and use locally suitable varieties where available."]
];

let currentCrop = "All";
let selectedImage = null;
let scans = 0;

function showPage(pageId) {
  document.querySelectorAll(".page").forEach(p => p.classList.remove("active"));
  document.querySelectorAll("nav button").forEach(b => b.classList.toggle("active", b.dataset.page === pageId));
  document.getElementById(pageId).classList.add("active");
  document.getElementById("breadcrumb").textContent =
    document.querySelector('nav button[data-page="' + pageId + '"]').textContent.trim();
  document.querySelector(".content").scrollIntoView({behavior:"smooth", block:"start"});
}

document.querySelectorAll("nav button").forEach(button => {
  button.addEventListener("click", () => showPage(button.dataset.page));
});

document.getElementById("themeButton").addEventListener("click", () => {
  document.body.classList.toggle("dark");
});

document.getElementById("languageButton").addEventListener("click", () => {
  alert("Hindi language support can be added to the interface. Disease names and scientific guidance are currently displayed in English.");
});

function renderGuide() {
  const search = document.getElementById("searchInput").value.toLowerCase().trim();
  const filtered = diseases.filter(d => {
    const matchesCrop = currentCrop === "All" || d.crop === currentCrop;
    const text = [d.crop,d.name,d.symptoms,d.about,...d.treatment,...d.prevention].join(" ").toLowerCase();
    return matchesCrop && text.includes(search);
  });

  const cards = document.getElementById("diseaseList");
  const treatment = document.getElementById("treatmentList");
  cards.innerHTML = "";
  treatment.innerHTML = "";

  if (!filtered.length) {
    cards.innerHTML = "<p>No matching conditions found. Try another search.</p>";
    return;
  }

  filtered.forEach((d, index) => {
    const card = document.createElement("article");
    card.className = "disease-card";
    card.innerHTML = `
      <div style="font-size:30px">${d.emoji}</div>
      <p>${d.crop}</p>
      <h3>${d.name}</h3>
      <p>${d.symptoms}</p>
      <button class="primary" type="button">View guidance</button>`;
    card.querySelector("button").addEventListener("click", () => {
      const details = document.getElementById("details-" + index);
      details.open = true;
      details.scrollIntoView({behavior:"smooth",block:"center"});
    });
    cards.appendChild(card);

    const detail = document.createElement("details");
    detail.id = "details-" + index;
    detail.innerHTML = `
      <summary>${d.crop} — ${d.name}</summary>
      <p><strong>About:</strong> ${d.about}</p>
      <p><strong>Common symptoms:</strong> ${d.symptoms}</p>
      <p><strong>Treatment / care:</strong></p>
      <ul>${d.treatment.map(x => "<li>"+x+"</li>").join("")}</ul>
      <p><strong>Prevention:</strong></p>
      <ul>${d.prevention.map(x => "<li>"+x+"</li>").join("")}</ul>`;
    treatment.appendChild(detail);
  });
}

document.getElementById("searchInput").addEventListener("input", renderGuide);

document.querySelectorAll(".filter").forEach(button => {
  button.addEventListener("click", () => {
    currentCrop = button.dataset.crop;
    document.querySelectorAll(".filter").forEach(b => b.classList.toggle("active", b === button));
    renderGuide();
  });
});

function renderTips() {
  const list = document.getElementById("tipsList");
  tips.forEach(tip => {
    const card = document.createElement("article");
    card.className = "disease-card";
    card.innerHTML = `<div style="font-size:30px">${tip[0]}</div><h3>${tip[1]}</h3><p>${tip[2]}</p>`;
    list.appendChild(card);
  });
}

const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");

imageInput.addEventListener("change", () => {
  selectedImage = imageInput.files[0] || null;
  if (!selectedImage) return;

  if (!selectedImage.type.startsWith("image/")) {
    alert("Please select an image file.");
    selectedImage = null;
    return;
  }

  preview.src = URL.createObjectURL(selectedImage);
  preview.classList.remove("hidden");
  document.getElementById("uploadMessage").textContent = "Selected: " + selectedImage.name;
  document.getElementById("resultPanel").classList.add("hidden");
});

document.getElementById("analyzeButton").addEventListener("click", async () => {
  if (!selectedImage) {
    alert("Please choose a leaf image first.");
    return;
  }

  const button = document.getElementById("analyzeButton");
  button.disabled = true;
  button.textContent = "Analyzing...";

  try {
    const formData = new FormData();
    formData.append("image", selectedImage);

    const response = await fetch(API_BASE + "/predict", {
      method: "POST",
      body: formData
    });

    if (!response.ok) throw new Error("Backend returned status " + response.status);

    const data = await response.json();
    const disease = data.label || data.disease || data.prediction || data.class_name;

    if (!disease) {
      throw new Error("The backend response did not include a disease label.");
    }

    const confidence = Number(data.confidence ?? data.confidence_score ?? 0);
    const normalizedConfidence = confidence <= 1 ? confidence * 100 : confidence;

    document.getElementById("resultImage").src = preview.src;
    document.getElementById("resultDisease").textContent = disease;
    document.getElementById("resultConfidence").textContent =
      "Model confidence: " + normalizedConfidence.toFixed(1) + "%";

    const matching = diseases.find(d => data.crop && data.condition
      ? (d.crop === data.crop && d.name === data.condition)
      : (disease.toLowerCase().includes(d.name.toLowerCase()) || d.name.toLowerCase().includes(disease.toLowerCase())));

    document.getElementById("resultAdvice").innerHTML = matching
      ? "<h3>General guidance</h3><p>" + matching.about + "</p><ul>" +
        matching.treatment.map(x => "<li>" + x + "</li>").join("") + "</ul>"
      : "<p>Review the Disease & Treatment Guide for general information. This prediction needs careful interpretation.</p>";

    if (normalizedConfidence < 60) {
      document.getElementById("resultAdvice").insertAdjacentHTML("afterbegin",
        "<p><strong>Not very sure.</strong> Confidence is below 60%. Try a clearer, closer photo of a single leaf.</p>");
    }
    document.getElementById("resultPanel").classList.remove("hidden");
    scans++;
    document.getElementById("scanCount").textContent = scans;

    const history = document.getElementById("history");
    if (scans === 1) history.innerHTML = "";
    const item = document.createElement("li");
    item.textContent = new Date().toLocaleString() + " — " + disease;
    history.prepend(item);

  } catch (error) {
    alert(
      "Could not analyze the image.\n\nMake sure the LeafCare server is running (python server.py) and open this page through it.\n\nDetails: " + error.message
    );
  } finally {
    button.disabled = false;
    button.textContent = "Analyze leaf";
  }
});

document.getElementById("clearHistory").addEventListener("click", () => {
  document.getElementById("history").innerHTML = '<li class="muted">No analyses yet.</li>';
  scans = 0;
  document.getElementById("scanCount").textContent = "0";
});

renderGuide();
renderTips();
</script>
</body>
</html>
