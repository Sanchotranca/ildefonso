<?php
// ============================================================
// enviar.php — Procesador de formulario de contacto
// Residencia Universitaria San Ildefonso UAH
// El correo destinatario vive aquí (lado servidor, nunca
// visible en el navegador).
// ============================================================

ini_set('session.cookie_httponly', 1);
ini_set('session.cookie_secure', 1);
ini_set('session.cookie_samesite', 'Lax');
session_start();

// ---------- Configuración ----------
$destino      = 'sanildefonso@crusa.es';                       // a quién llega la consulta
$remitente    = 'nocontestar@residenciasanildefonso.es';       // From: buzón real del dominio (SPF/DKIM)
$nombre_sitio = 'Residencia San Ildefonso';
$url_ok       = 'gracias.html';
$url_ko       = 'contacto.php?error=1';

// ---------- Solo POST ----------
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: ' . $url_ko);
    exit;
}

// ---------- CSRF token ----------
$csrf_recibido = $_POST['csrf_token'] ?? '';
$csrf_sesion   = $_SESSION['csrf_token'] ?? '';
if (!$csrf_sesion || !hash_equals($csrf_sesion, $csrf_recibido)) {
    header('Location: ' . $url_ko . '&motivo=csrf');
    exit;
}
// Rotación de token post-submit (previene doble envío)
$_SESSION['csrf_token'] = bin2hex(random_bytes(32));

// ---------- Honeypot anti-spam ----------
if (!empty($_POST['botcheck'])) {
    header('Location: ' . $url_ok); // El bot cree que funcionó; silencio.
    exit;
}

// ---------- CAPTCHA matemático ----------
$captcha_usuario = intval($_POST['captcha'] ?? -1);
$captcha_correcto = isset($_SESSION['captcha_res']) && $captcha_usuario === (int) $_SESSION['captcha_res'];
unset($_SESSION['captcha_res']); // Un solo uso
if (!$captcha_correcto) {
    header('Location: ' . $url_ko . '&motivo=captcha');
    exit;
}

// ---------- Sanitizar entradas ----------
// Elimina CR/LF (y sus formas URL-encoded) ANTES de htmlspecialchars
// para prevenir Mail Header Injection en Reply-To y otros headers.
function limpiar(string $val): string {
    $val = str_replace(["\r", "\n", "%0a", "%0d", "%0A", "%0D"], '', $val);
    return htmlspecialchars(strip_tags(trim($val)), ENT_QUOTES, 'UTF-8');
}

$nombre    = limpiar($_POST['nombre']    ?? '');
$apellidos = limpiar($_POST['apellidos'] ?? '');
$email     = filter_var(trim($_POST['email'] ?? ''), FILTER_VALIDATE_EMAIL);
$telefono  = limpiar($_POST['telefono']  ?? '');
$motivo    = limpiar($_POST['motivo']    ?? '');
$fecha_entrada = limpiar($_POST['fecha_entrada'] ?? '');
$fecha_salida  = limpiar($_POST['fecha_salida']  ?? '');
$mensaje   = limpiar($_POST['mensaje']   ?? '');

// ---------- Validar obligatorios ----------
if (!$nombre || !$email || !$mensaje) {
    header('Location: ' . $url_ko);
    exit;
}

// ---------- Construir email ----------
$asunto  = "Nueva consulta · {$nombre_sitio}";

$cuerpo  = "Nombre:    {$nombre} {$apellidos}\n";
$cuerpo .= "Email:     {$email}\n";
if ($telefono) $cuerpo .= "Teléfono:  {$telefono}\n";
if ($motivo)   $cuerpo .= "Motivo:    {$motivo}\n";
if ($fecha_entrada) $cuerpo .= "Entrada:   {$fecha_entrada}\n";
if ($fecha_salida)  $cuerpo .= "Salida:    {$fecha_salida}\n";
$cuerpo .= "\nMensaje:\n{$mensaje}\n";
$cuerpo .= "\n---\nEnviado desde el formulario web de {$nombre_sitio}.\n";

$cabeceras  = "From: {$nombre_sitio} <{$remitente}>\r\n";
$cabeceras .= "Reply-To: {$nombre} {$apellidos} <{$email}>\r\n";
$cabeceras .= "Content-Type: text/plain; charset=UTF-8\r\n";
$cabeceras .= "X-Mailer: PHP/" . phpversion() . "\r\n";

// ---------- Enviar ----------
$ok = mail($destino, '=?UTF-8?B?' . base64_encode($asunto) . '?=', $cuerpo, $cabeceras);

header('Location: ' . ($ok ? $url_ok : $url_ko));
exit;
