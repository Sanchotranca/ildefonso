<?php
// ============================================================
// enviar.php — Procesador de formulario de contacto
// Residencia Universitaria San Ildefonso UAH
// El correo destinatario vive aquí (lado servidor, nunca
// visible en el navegador).
// ============================================================

session_start();

// ---------- Configuración ----------
$destino      = 'sanildefonso@crusa.es';
$nombre_sitio = 'Residencia San Ildefonso';
$url_ok       = 'gracias.html';
$url_ko       = 'contacto.php?error=1';

// ---------- Solo POST ----------
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: ' . $url_ko);
    exit;
}

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
function limpiar(string $val): string {
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

$cabeceras  = "From: {$nombre_sitio} <{$destino}>\r\n";
$cabeceras .= "Reply-To: {$nombre} {$apellidos} <{$email}>\r\n";
$cabeceras .= "Content-Type: text/plain; charset=UTF-8\r\n";
$cabeceras .= "X-Mailer: PHP/" . phpversion() . "\r\n";

// ---------- Enviar ----------
$ok = 