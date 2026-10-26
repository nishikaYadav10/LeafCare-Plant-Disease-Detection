/* ================= CONFIG ================= */
// Put your backend URL here (Flask/FastAPI). Leave empty to run in DEMO mode.
// Expected JSON response: { "label": "potato_early_blight", "confidence": 0.93, "severity": 18.4 }
const API_URL = "/predict";            // e.g. "http://localhost:5000/predict"
const CONF_THRESHOLD = 0.60;   // below this -> "not sure"
const MODEL_ACCURACY = "";     // e.g. "94.2% accuracy" (shown in the sidebar)

/* ================= TEXT (English + Hindi) ================= */
const T = {
  en:{tagline:"AI Plant Health & Advisory",navDash:"Dashboard",navAnalyze:"Analyze Plant",navKnow:"Knowledge Base",navDis:"Common Diseases",navTreat:"Treatment Guide",navTips:"Tips & Prevention",engine:"AI Engine Live",analyzeNow:"＋ Analyze Plant",
    heroA:"Let's keep your",heroB:"plants healthy.",heroSub:"Upload a leaf photo. LeafCare identifies the condition, shows how badly the leaf is affected, and gives simple treatment advice.",
    dropTitle:"Drag & drop a leaf image here",or:"or",browse:"click to browse",fromDevice:"from your device",orChoose:"or choose below",chooseFile:"Choose File",takePhoto:"Take Photo",tryDemo:"Try Demo",
    guardTag:"GUARDRAIL ACTIVE",guardText:"LeafCare asks for a retake when it is not confident, so unclear or non-leaf photos do not get a wrong disease label.",
    stClasses:"Classes detected",stCrops:"Crops supported",stScans:"Scans done",stThr:"Min. confidence",howTitle:"How it works",h1:"Take or upload a leaf photo",h2:"AI predicts the disease with a confidence score",h3:"Severity is estimated from the affected leaf area",h4:"Get treatment and prevention steps",
    recent:"Recent scans",clear:"Clear",noScans:"No scans yet. Try your first leaf!",
    tip1:"Show only one leaf, filling most of the photo",tip2:"Use daylight, avoid shadows",tip3:"Keep the photo sharp, not blurry",analyze:"🔍 Analyze leaf",
    uncTitle:"We are not sure",uncText:"The photo is not clear enough. Please retake it in good light with one leaf filling the frame.",retake:"Try another photo",crop:"Crop",disease:"Result",conf:"confident",
    sevTitle:"How badly is the leaf affected?",mild:"Mild",moderate:"Moderate",severe:"Severe",sevOf:"of the leaf is affected —",advTitle:"What should I do?",tAbout:"About",tTreat:"Treatment",tPrevent:"Prevention",
    disc:"This is guidance only. For chemical sprays, check dose and safety with your local agriculture officer or Krishi Vigyan Kendra (KVK).",another:"Check another leaf",share:"Share result",
    knowSub:"Search everything LeafCare knows about potato and tomato leaf conditions.",search:"Search disease or crop…",disSub:"Diseases LeafCare can detect. Tap a card for details.",all:"All",potato:"Potato",tomato:"Tomato",
    treatSub:"Step-by-step care for each disease. Tap to open.",tipsSub:"Simple habits that keep your crop healthy.",close:"Close",
    healthy:"Healthy",needAction:"Needs care",urgent:"Act quickly",disBadge:"Disease",msg1:"Reading your leaf…",msg2:"Finding the disease…",msg3:"Measuring the damage…",msg4:"Preparing advice…",
    pickFirst:"Please choose a photo first",notImage:"Please choose an image file",netErr:"Could not reach the server. Try again.",copied:"Result copied",
    lblMild:"Mild",lblModerate:"Moderate",lblSevere:"Severe",langBtn:"हिंदी",g1:"Good morning!",g2:"Good afternoon!",g3:"Good evening!",classes:"7 classes",demo:"Demo",live:"Ready"},
  hi:{tagline:"AI पौध स्वास्थ्य एवं सलाह",navDash:"डैशबोर्ड",navAnalyze:"पौधा जाँचें",navKnow:"ज्ञान भंडार",navDis:"आम बीमारियाँ",navTreat:"इलाज गाइड",navTips:"सुझाव व बचाव",engine:"AI इंजन चालू",analyzeNow:"＋ पौधा जाँचें",
    heroA:"आइए आपके",heroB:"पौधे स्वस्थ रखें।",heroSub:"पत्ते की फोटो डालें। LeafCare बीमारी पहचानेगा, नुकसान बताएगा और इलाज की आसान सलाह देगा।",
    dropTitle:"पत्ते की फोटो यहाँ डालें",or:"या",browse:"क्लिक करके चुनें",fromDevice:"अपने फोन/कंप्यूटर से",orChoose:"या नीचे से चुनें",chooseFile:"फाइल चुनें",takePhoto:"फोटो खींचें",tryDemo:"डेमो देखें",
    guardTag:"सुरक्षा जाँच चालू",guardText:"भरोसा कम होने पर LeafCare दोबारा फोटो माँगता है, ताकि धुंधली या पत्ते के अलावा फोटो पर गलत बीमारी न बताए।",
    stClasses:"पहचानी जाने वाली श्रेणियाँ",stCrops:"समर्थित फसलें",stScans:"जाँच हुई",stThr:"न्यूनतम भरोसा",howTitle:"यह कैसे काम करता है",h1:"पत्ते की फोटो लें या डालें",h2:"AI भरोसे के साथ बीमारी बताता है",h3:"प्रभावित हिस्से से गंभीरता का अनुमान",h4:"इलाज और बचाव के उपाय पाएँ",
    recent:"हाल की जाँच",clear:"मिटाएँ",noScans:"अभी कोई जाँच नहीं। अपना पहला पत्ता आज़माएँ!",
    tip1:"सिर्फ एक पत्ता दिखाएँ, फोटो में पूरा भरा हो",tip2:"दिन की रोशनी में लें, छाया से बचें",tip3:"फोटो साफ हो, धुंधली न हो",analyze:"🔍 पत्ता जाँचें",
    uncTitle:"हमें पक्का नहीं पता",uncText:"फोटो साफ़ नहीं है। कृपया अच्छी रोशनी में एक पत्ते की दोबारा फोटो लें।",retake:"दूसरी फोटो लें",crop:"फसल",disease:"नतीजा",conf:"भरोसा",
    sevTitle:"पत्ता कितना प्रभावित है?",mild:"हल्का",moderate:"मध्यम",severe:"गंभीर",sevOf:"पत्ता प्रभावित है —",advTitle:"मुझे क्या करना चाहिए?",tAbout:"जानकारी",tTreat:"इलाज",tPrevent:"बचाव",
    disc:"यह केवल सलाह है। रासायनिक दवा की मात्रा और सुरक्षा के लिए अपने कृषि अधिकारी या कृषि विज्ञान केंद्र (KVK) से पूछें।",another:"दूसरा पत्ता जाँचें",share:"नतीजा साझा करें",
    knowSub:"आलू और टमाटर के पत्तों की स्थितियों के बारे में सब कुछ खोजें।",search:"बीमारी या फसल खोजें…",disSub:"LeafCare जो बीमारियाँ पहचान सकता है। विवरण के लिए कार्ड दबाएँ।",all:"सभी",potato:"आलू",tomato:"टमाटर",
    treatSub:"हर बीमारी के लिए चरणबद्ध देखभाल। खोलने के लिए दबाएँ।",tipsSub:"आसान आदतें जो फसल को स्वस्थ रखती हैं।",close:"बंद करें",
    healthy:"स्वस्थ",needAction:"देखभाल ज़रूरी",urgent:"जल्दी कदम उठाएँ",disBadge:"बीमारी",msg1:"पत्ता पढ़ रहे हैं…",msg2:"बीमारी खोज रहे हैं…",msg3:"नुकसान नाप रहे हैं…",msg4:"सलाह तैयार कर रहे हैं…",
    pickFirst:"पहले फोटो चुनें",notImage:"कृपया इमेज फाइल चुनें",netErr:"सर्वर से जुड़ नहीं पाए। दोबारा कोशिश करें।",copied:"नतीजा कॉपी हुआ",
    lblMild:"हल्का",lblModerate:"मध्यम",lblSevere:"गंभीर",langBtn:"English",g1:"सुप्रभात!",g2:"नमस्कार!",g3:"शुभ संध्या!",classes:"7 श्रेणियाँ",demo:"डेमो",live:"तैयार"}
};

/* ================= HELPERS ================= */
const $ = s => document.querySelector(s);
const $$ = s => document.querySelectorAll(s);
let lang = localStorage.getItem("lc_lang") || "en";
let file = null, current = null, currentTab = "about", cropFilter = "all", imgURL = "";

const t = k => (T[lang][k] ?? T.en[k] ?? k);
function toast(msg){ const el=$("#toast"); el.textContent=msg; el.hidden=false; setTimeout(()=>el.hidden=true,2600); }
function esc(s){ return String(s).replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c])); }
function ul(arr, cls){ return `<ul class="${cls}">${arr.map(x=>`<li>${esc(x)}</li>`).join("")}</ul>`; }

/* ================= THEME & LANGUAGE ================= */
function setTheme(th){
  document.documentElement.dataset.theme = th;
  localStorage.setItem("lc_theme", th);
  $("#themeBtn").textContent = th==="dark" ? "☀️" : "🌙";
}
setTheme(localStorage.getItem("lc_theme") || (matchMedia("(prefers-color-scheme:dark)").matches ? "dark" : "light"));
$("#themeBtn").onclick = () => setTheme(document.documentElement.dataset.theme==="dark" ? "light" : "dark");

function greeting(){
  const h = new Date().getHours();
  return t(h<12 ? "g1" : h<17 ? "g2" : "g3").toUpperCase();
}

function applyLang(){
  document.documentElement.lang = lang;
  $$("[data-i18n]").forEach(el => el.textContent = t(el.dataset.i18n));
  $("#langBtn").textContent = t("langBtn");
  $("#search").placeholder = t("search");
  $("#greet").textContent = greeting();
  $("#engineState").textContent = API_URL ? t("live") : t("demo");
  $("#modelAcc").textContent = MODEL_ACCURACY || t("classes");
  updateCrumb(); renderLists(); renderHistory();
  if(current) renderResult(current);
}
$("#langBtn").onclick = () => { lang = lang==="en" ? "hi" : "en"; localStorage.setItem("lc_lang",lang); applyLang(); };

/* ================= ROUTER (pages) ================= */
const PAGES = ["dashboard","analyze","knowledge","diseases","treatment","tips"];
const NAVKEY = {dashboard:"navDash",analyze:"navAnalyze",knowledge:"navKnow",diseases:"navDis",treatment:"navTreat",tips:"navTips"};
function updateCrumb(){ $("#crumb").textContent = t(NAVKEY[pageNow()]); }
function pageNow(){ const p = location.hash.slice(1); return PAGES.includes(p) ? p : "dashboard"; }
function route(){
  const p = pageNow();
  PAGES.forEach(id => $("#"+id).hidden = id!==p);
  $$("#nav a").forEach(a => a.classList.toggle("active", a.dataset.page===p));
  updateCrumb(); closeMenu(); window.scrollTo({top:0});
}
window.addEventListener("hashchange", route);

const openMenu = () => { $("#sidebar").classList.add("open"); $("#scrim").classList.add("show"); };
const closeMenu = () => { $("#sidebar").classList.remove("open"); $("#scrim").classList.remove("show"); };
$("#menuBtn").onclick = openMenu;
$("#scrim").onclick = closeMenu;

/* ================= IMAGE INPUT ================= */
function setFile(f){
  if(!f) return;
  if(!f.type.startsWith("image/")) return toast(t("notImage"));
  if(imgURL) URL.revokeObjectURL(imgURL);
  file = f; imgURL = URL.createObjectURL(f);
  const img = $("#preview");
  img.src = imgURL; img.hidden = false;
  $("#dropText").hidden = true;
  $("#analyzeBtn").disabled = false;
}
function bindDrop(box, onFile, clickInput){
  ["dragenter","dragover"].forEach(ev => box.addEventListener(ev, e => { e.preventDefault(); box.classList.add("over"); }));
  ["dragleave","drop"].forEach(ev => box.addEventListener(ev, e => { e.preventDefault(); box.classList.remove("over"); }));
  box.addEventListener("drop", e => onFile(e.dataTransfer.files[0]));
  box.addEventListener("click", e => { if(!e.target.closest("label,button")) clickInput.click(); });
  box.addEventListener("keydown", e => { if(e.key==="Enter") clickInput.click(); });
}
// Analyze page inputs
$("#fileInput").onchange = e => setFile(e.target.files[0]);
$("#camInput").onchange  = e => setFile(e.target.files[0]);
bindDrop($("#drop"), setFile, $("#fileInput"));
// Dashboard inputs -> jump to Analyze page with the photo ready
const fromDash = f => { if(!f) return; setFile(f); location.hash = "analyze"; };
$("#dashFile").onchange = e => fromDash(e.target.files[0]);
$("#dashCam").onchange  = e => fromDash(e.target.files[0]);
bindDrop($("#dashDrop"), fromDash, $("#dashFile"));

// Demo: draws a simple leaf-like picture so you can test without a photo
$("#demoBtn").onclick = () => {
  const c = document.createElement("canvas"); c.width = c.height = 400;
  const x = c.getContext("2d");
  x.fillStyle = "#dfe9d6"; x.fillRect(0,0,400,400);
  x.fillStyle = "#3f8f3f"; x.beginPath(); x.ellipse(200,200,120,170,Math.PI/6,0,7); x.fill();
  x.fillStyle = "#7a5230"; for(let i=0;i<9;i++){ x.beginPath(); x.arc(150+Math.random()*100,120+Math.random()*160,8+Math.random()*14,0,7); x.fill(); }
  c.toBlob(b => fromDash(new File([b],"demo-leaf.png",{type:"image/png"})));
};

/* ================= PREDICTION ================= */
function shrink(f, max=800){   // smaller upload = faster on slow rural networks
  return new Promise(res => {
    const img = new Image();
    img.onload = () => {
      const r = Math.min(1, max/Math.max(img.width,img.height));
      const c = document.createElement("canvas");
      c.width = img.width*r; c.height = img.height*r;
      c.getContext("2d").drawImage(img,0,0,c.width,c.height);
      c.toBlob(b => res(b || f), "image/jpeg", .85);
    };
    img.onerror = () => res(f);
    img.src = URL.createObjectURL(f);
  });
}
async function predict(f){
  if(!API_URL){                                   // DEMO MODE (no backend yet)
    await new Promise(r => setTimeout(r, 1800));
    const keys = Object.keys(KB);
    const label = keys[Math.floor(Math.random()*keys.length)];
    return { label, confidence: 0.75 + Math.random()*0.24, severity: KB[label].healthy ? 0 : 5 + Math.random()*45 };
  }
  const fd = new FormData();
  fd.append("image", await shrink(f), "leaf.jpg");
  const r = await fetch(API_URL, { method:"POST", body:fd });
  if(!r.ok) throw new Error("server");
  return r.json();
}

$("#analyzeBtn").onclick = async () => {
  if(!file) return toast(t("pickFirst"));
  $("#uploadCard").hidden = true; $("#result").hidden = true; $("#loading").hidden = false;
  const msgs = ["msg1","msg2","msg3","msg4"]; let i = 0;
  $("#loadMsg").textContent = t(msgs[0]);
  const timer = setInterval(() => $("#loadMsg").textContent = t(msgs[++i % 4]), 900);
  try{
    current = await predict(file);
    saveHistory(current);
    renderResult(current, true);
  }catch(e){
    toast(t("netErr")); $("#uploadCard").hidden = false;
  }finally{
    clearInterval(timer); $("#loading").hidden = true;
  }
};

/* ================= RESULT ================= */
const sevLevel = p => p<10 ? "Mild" : p<30 ? "Moderate" : "Severe";
const barPos = p => p<10 ? p/10*33 : p<30 ? 33+(p-10)/20*33 : 66+Math.min((p-30)/30,1)*34;

function renderResult(r, scroll){
  const info = KB[r.label];
  $("#result").hidden = false;
  const unsure = !info || r.confidence < CONF_THRESHOLD;
  $("#uncertain").hidden = !unsure;
  $("#resultBody").hidden = unsure;
  if(unsure) return;

  const sev = r.severity || 0;
  const level = info.healthy ? "ok" : (info.urgent || sev>=30 ? "bad" : "warn");
  $("#resImg").src = imgURL;
  $("#rCrop").textContent = info.cropName[lang];
  $("#rDisease").textContent = info.name[lang];
  const pill = $("#rStatus");
  pill.className = "pill " + (level==="ok" ? "" : level);
  pill.textContent = level==="ok" ? t("healthy") : level==="bad" ? t("urgent") : t("needAction");
  $("#verdictCard").className = "panel verdict " + (level==="ok" ? "" : level);

  $("#rConf").textContent = Math.round(r.confidence*100) + "%";
  const fg = $("#ringFg");
  fg.style.stroke = level==="bad" ? "var(--bad)" : level==="warn" ? "var(--warn)" : "var(--g)";
  requestAnimationFrame(() => fg.style.strokeDashoffset = 327 - 327*r.confidence);

  $("#sevCard").hidden = !!info.healthy;
  if(!info.healthy){
    $("#sevPct").textContent = sev.toFixed(0) + "%";
    $("#sevLabel").textContent = t("lbl" + sevLevel(sev));
    requestAnimationFrame(() => $("#sevFill").style.left = barPos(sev) + "%");
  }
  showTab(currentTab);
  if(scroll) $("#result").scrollIntoView({behavior:"smooth"});
}
function showTab(tab){
  currentTab = tab;
  $$(".tab").forEach(b => b.classList.toggle("active", b.dataset.tab===tab));
  if(current && KB[current.label]) $("#advList").innerHTML = KB[current.label][tab][lang].map(x=>`<li>${esc(x)}</li>`).join("");
}
$$(".tab").forEach(b => b.onclick = () => showTab(b.dataset.tab));

function resetAnalyze(){
  file = null; current = null; currentTab = "about";
  $("#preview").hidden = true; $("#preview").src = "";
  $("#dropText").hidden = false; $("#analyzeBtn").disabled = true;
  ["fileInput","camInput","dashFile","dashCam"].forEach(id => $("#"+id).value = "");
  $("#result").hidden = true; $("#uploadCard").hidden = false;
  $("#ringFg").style.strokeDashoffset = 327; $("#sevFill").style.left = "0%";
  window.scrollTo({top:0,behavior:"smooth"});
}
$("#againBtn").onclick = resetAnalyze;
$("#retakeBtn").onclick = resetAnalyze;

$("#shareBtn").onclick = async () => {
  if(!current) return;
  const i = KB[current.label];
  const text = `LeafCare: ${i.cropName[lang]} – ${i.name[lang]} (${Math.round(current.confidence*100)}%)` +
    (i.healthy ? "" : `\n${t("sevTitle")} ${Math.round(current.severity)}%`) + `\n${i.treat[lang].join("\n")}`;
  if(navigator.share){ try{ await navigator.share({title:"LeafCare", text}); }catch(e){} }
  else { try{ await navigator.clipboard.writeText(text); toast(t("copied")); }catch(e){ toast(text); } }
};

/* ================= HISTORY (saved in this browser) ================= */
function getHistory(){ try{ return JSON.parse(localStorage.getItem("lc_hist")||"[]"); }catch(e){ return []; } }
function saveHistory(r){
  if(!KB[r.label] || r.confidence < CONF_THRESHOLD) return;
  const h = getHistory(); h.unshift({label:r.label, conf:r.confidence, date:Date.now()});
  try{ localStorage.setItem("lc_hist", JSON.stringify(h.slice(0,20))); }catch(e){}
  renderHistory();
}
function renderHistory(){
  const h = getHistory();
  $("#scanCount").textContent = h.length;
  $("#history").innerHTML = h.length
    ? h.slice(0,5).map(x => `<li><span>${KB[x.label].emoji} ${esc(KB[x.label].name[lang])}</span><small>${Math.round(x.conf*100)}% · ${new Date(x.date).toLocaleDateString()}</small></li>`).join("")
    : `<li class="empty">${esc(t("noScans"))}</li>`;
}
$("#clearHist").onclick = () => { try{ localStorage.removeItem("lc_hist"); }catch(e){} renderHistory(); };

/* ================= INFO PAGES ================= */
function badge(i){
  return i.healthy ? `<span class="badge">${t("healthy")}</span>` : i.urgent ? `<span class="badge bad">${t("urgent")}</span>` : `<span class="badge warn">${t("disBadge")}</span>`;
}
function cardHTML(key){
  const i = KB[key];
  return `<button class="card" data-key="${key}"><span class="emoji">${i.emoji}</span><h3>${esc(i.name[lang])}</h3><p>${esc(i.cropName[lang])} · ${esc(i.about[lang][0])}</p>${badge(i)}</button>`;
}
function renderLists(){
  const q = $("#search").value.trim().toLowerCase();
  $("#knowList").innerHTML = Object.keys(KB)
    .filter(k => !q || (KB[k].name.en+KB[k].name.hi+KB[k].cropName.en+KB[k].cropName.hi).toLowerCase().includes(q))
    .map(cardHTML).join("") || `<p class="empty">—</p>`;

  const diseases = Object.keys(KB).filter(k => !KB[k].healthy && (cropFilter==="all" || KB[k].crop===cropFilter));
  $("#disList").innerHTML = diseases.map(cardHTML).join("");

  $("#treatList").innerHTML = Object.keys(KB).filter(k => !KB[k].healthy).map(k => {
    const i = KB[k];
    return `<details><summary><span>${i.emoji} ${esc(i.name[lang])}</span></summary><div class="body">
      <h4>${t("tTreat")}</h4>${ul(i.treat[lang],"steps")}<h4>${t("tPrevent")}</h4>${ul(i.prevent[lang],"steps")}</div></details>`;
  }).join("");

  $("#tipsList").innerHTML = TIPS.map(x => `<div class="card static"><span class="emoji">${x.e}</span><h3>${esc(x[lang][0])}</h3><p>${esc(x[lang][1])}</p></div>`).join("");
}
$("#search").oninput = renderLists;
$$(".chip-btn").forEach(b => b.onclick = () => {
  cropFilter = b.dataset.crop;
  $$(".chip-btn").forEach(x => x.classList.toggle("active", x===b));
  renderLists();
});

/* detail popup for cards */
document.addEventListener("click", e => {
  const c = e.target.closest(".card[data-key]");
  if(!c) return;
  const i = KB[c.dataset.key];
  $("#modalBody").innerHTML = `<h2>${i.emoji} ${esc(i.name[lang])}</h2><p class="label">${esc(i.cropName[lang])}</p>
    <h4>${t("tAbout")}</h4>${ul(i.about[lang],"steps")}
    <h4>${t("tTreat")}</h4>${ul(i.treat[lang],"steps")}
    <h4>${t("tPrevent")}</h4>${ul(i.prevent[lang],"steps")}`;
  $("#modal").showModal();
});
$("#closeModal").onclick = () => $("#modal").close();
$("#modal").addEventListener("click", e => { if(e.target.id==="modal") e.target.close(); });

/* ================= START ================= */
applyLang();
route();