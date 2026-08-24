// forms.js — formularios de brain-labs.io sobre Supabase.
// Un solo archivo para las tres paginas. Cada <form> se configura
// con data-table, data-lang y data-cv.
//
// La anon key es publica por diseno: la defensa real son las
// politicas RLS, que solo permiten INSERT y ninguna lectura.

import { createClient } from 'https://esm.sh/@supabase/supabase-js@2.112.4';

const SUPABASE_URL = 'https://vksrqmipvxjgavmfgoql.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZrc3JxbWlwdnhqZ2F2bWZnb3FsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODc1MDk0NTQsImV4cCI6MjEwMzA4NTQ1NH0.Oubk6kxubCtw7jvIDOBC7fFCUUZxP4MRmqUDMJwkA9Q';

const CONTACT_EMAIL = 'veronica@brain-labs.io';
const CV_BUCKET = 'cvs';
const CV_MAX_BYTES = 5 * 1024 * 1024;
const CV_EXTENSIONS = ['pdf', 'doc', 'docx'];
const CV_MIME = [
  'application/pdf',
  'application/msword',
  'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
];

const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
  auth: { persistSession: false, autoRefreshToken: false }
});

const COPY = {
  en: {
    sending: 'Sending…',
    okTitle: 'Thanks — we have it.',
    okBodyApp: 'We review every application. If your experience fits something we have open, you will hear from us at the email you gave us.',
    okBodyReq: 'We will come back to you within one business day at the email you gave us.',
    okNoCv: 'Heads up: your CV could not be attached, so we saved your application without it. You can email it to ' + CONTACT_EMAIL + ' and we will match it up.',
    errGeneric: 'Something went wrong on our side and your submission was not saved.',
    errNetwork: 'We could not reach our servers. Check your connection and try again.',
    errMailto: 'You can also email us directly at',
    cvTooBig: 'That file is larger than 5 MB. Please upload a smaller version.',
    cvBadType: 'Please upload a PDF, DOC or DOCX file.',
    cvEmpty: 'That file appears to be empty.',
    linkedinBad: 'That does not look like a LinkedIn profile URL.'
  },
  es: {
    sending: 'Enviando…',
    okTitle: 'Listo — ya nos llegó.',
    okBodyApp: 'Revisamos todas las postulaciones. Si tu experiencia calza con algo que tengamos abierto, te escribimos al correo que nos dejaste.',
    okBodyReq: 'Te respondemos dentro de un día hábil al correo que nos dejaste.',
    okNoCv: 'Un aviso: no pudimos adjuntar tu CV, así que guardamos la postulación sin él. Puedes mandarlo a ' + CONTACT_EMAIL + ' y lo juntamos.',
    errGeneric: 'Hubo un problema de nuestro lado y tu envío no se guardó.',
    errNetwork: 'No pudimos conectar con nuestros servidores. Revisa tu conexión e intenta de nuevo.',
    errMailto: 'También puedes escribirnos directo a',
    cvTooBig: 'Ese archivo pesa más de 5 MB. Sube una versión más liviana.',
    cvBadType: 'Sube un archivo PDF, DOC o DOCX.',
    cvEmpty: 'Ese archivo parece estar vacío.',
    linkedinBad: 'Eso no parece una URL de perfil de LinkedIn.'
  }
};

// ---------- utilidades ----------

// '' -> null. Los campos opcionales tienen CHECK que rechaza la
// cadena vacia, asi que mandarla romperia el insert.
const clean = (v) => {
  if (typeof v !== 'string') return v ?? null;
  const t = v.trim();
  return t === '' ? null : t;
};

const uuid = () =>
  (crypto.randomUUID
    ? crypto.randomUUID()
    : 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, (c) => {
        const r = (Math.random() * 16) | 0;
        return (c === 'x' ? r : (r & 0x3) | 0x8).toString(16);
      }));

// El nombre final debe encajar con la policy de storage:
// ^{uuid}-[A-Za-z0-9._-]{1,120}$
function safeFileName(original) {
  const dot = original.lastIndexOf('.');
  const ext = (dot > -1 ? original.slice(dot + 1) : '').toLowerCase().replace(/[^a-z0-9]/g, '');
  const base = (dot > -1 ? original.slice(0, dot) : original)
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')   // saca acentos
    .replace(/[^A-Za-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .slice(0, 80);
  const name = (base || 'cv') + (ext ? '.' + ext : '');
  return name.slice(0, 120);
}

function normalizeLinkedin(v) {
  const t = clean(v);
  if (!t) return null;
  return /^https?:\/\//i.test(t) ? t : 'https://' + t.replace(/^\/+/, '');
}

function fileError(file, t) {
  const ext = file.name.split('.').pop().toLowerCase();
  if (file.size === 0) return t.cvEmpty;
  if (file.size > CV_MAX_BYTES) return t.cvTooBig;
  if (!CV_EXTENSIONS.includes(ext)) return t.cvBadType;
  // El tipo puede venir vacio en algunos navegadores; ahi confiamos
  // en la extension y en el allowed_mime_types del bucket.
  if (file.type && !CV_MIME.includes(file.type)) return t.cvBadType;
  return null;
}

// ---------- UI ----------

function showMessage(form, html) {
  const box = form.querySelector('[data-msg]');
  box.innerHTML = html;
  box.hidden = false;
  box.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

function clearMessage(form) {
  const box = form.querySelector('[data-msg]');
  box.innerHTML = '';
  box.hidden = true;
}

function showError(form, t, message) {
  showMessage(
    form,
    `<p>${message}</p><p>${t.errMailto} <a href="mailto:${CONTACT_EMAIL}">${CONTACT_EMAIL}</a>.</p>`
  );
}

function showSuccess(form, t, body, extra) {
  const wrap = form.parentElement;
  const panel = document.createElement('div');
  panel.className = 'bl-success';
  panel.setAttribute('role', 'status');
  panel.innerHTML =
    `<h3>${t.okTitle}</h3><p>${body}</p>` + (extra ? `<p class="bl-note">${extra}</p>` : '');
  form.replaceWith(panel);
  wrap.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

function setLoading(form, on, t) {
  const btn = form.querySelector('[data-submit]');
  if (on) {
    btn.dataset.label = btn.textContent;
    btn.textContent = t.sending;
    btn.disabled = true;
    form.setAttribute('aria-busy', 'true');
  } else {
    btn.textContent = btn.dataset.label || btn.textContent;
    btn.disabled = false;
    form.removeAttribute('aria-busy');
  }
}

// ---------- envio ----------

async function handleSubmit(event) {
  const form = event.target;
  event.preventDefault();

  const t = COPY[form.dataset.lang === 'es' ? 'es' : 'en'];
  const table = form.dataset.table;
  clearMessage(form);

  // Honeypot: un bot rellena todo. Fingimos exito y no guardamos nada.
  if (form.querySelector('[name="_hp"]').value !== '') {
    showSuccess(form, t, table === 'applications' ? t.okBodyApp : t.okBodyReq, '');
    return;
  }

  if (!form.checkValidity()) {
    form.reportValidity();
    return;
  }

  const fileInput = form.querySelector('input[type="file"]');
  const file = fileInput && fileInput.files.length ? fileInput.files[0] : null;

  if (file) {
    const err = fileError(file, t);
    if (err) {
      showMessage(form, `<p>${err}</p>`);
      fileInput.focus();
      return;
    }
  }

  // Payload: los name= del formulario coinciden con las columnas.
  const payload = {};
  for (const [key, value] of new FormData(form).entries()) {
    if (key === '_hp' || key === 'cv') continue;
    payload[key] = clean(value);
  }
  if ('linkedin_url' in payload) {
    payload.linkedin_url = normalizeLinkedin(payload.linkedin_url);
    if (payload.linkedin_url && !/linkedin\.com\//i.test(payload.linkedin_url)) {
      showMessage(form, `<p>${t.linkedinBad}</p>`);
      form.querySelector('[name="linkedin_url"]').focus();
      return;
    }
  }

  setLoading(form, true, t);

  let cvFailed = false;
  try {
    if (file) {
      const path = `${uuid()}-${safeFileName(file.name)}`;
      const up = await supabase.storage
        .from(CV_BUCKET)
        .upload(path, file, { contentType: file.type || 'application/octet-stream', upsert: false });

      if (up.error) {
        // El CV es opcional: preferimos guardar la postulacion sin
        // archivo antes que perder al candidato por un fallo de red.
        cvFailed = true;
        console.warn('CV upload failed:', up.error.message);
      } else {
        payload.cv_path = up.data.path;
      }
    }

    // Sin .select(): anon no tiene privilegio de SELECT y pedir la
    // representacion devolveria 42501.
    const { error } = await supabase.from(table).insert(payload);
    if (error) throw error;

    showSuccess(
      form,
      t,
      table === 'applications' ? t.okBodyApp : t.okBodyReq,
      cvFailed ? t.okNoCv : ''
    );
  } catch (err) {
    setLoading(form, false, t);
    const offline = !navigator.onLine || /fetch|network|failed to fetch/i.test(err.message || '');
    showError(form, t, offline ? t.errNetwork : t.errGeneric);
    console.error('Submit failed:', err);
  }
}

document.querySelectorAll('form[data-table]').forEach((form) => {
  form.addEventListener('submit', handleSubmit);
  // Limpiamos el mensaje de error apenas el usuario corrige algo.
  form.addEventListener('input', () => clearMessage(form), { once: false });
});
