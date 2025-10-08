#!/usr/bin/env python3
"""
Script para crear instaladores multiplataforma de MarkdownViewer
Genera ejecutables autocontenidos para Windows, Linux y macOS
"""

import os
import sys
import platform
import subprocess
import shutil
from pathlib import Path

VERSION = "1.0.0"
APP_NAME = "MarkdownViewer"

def clean_build_dirs():
    """Limpiar directorios de build anteriores"""
    print("[*] Limpiando directorios de build...")
    for dir_name in ['build', 'dist']:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"   Eliminado: {dir_name}/")

def install_dependencies():
    """Instalar dependencias necesarias"""
    print("[*] Desinstalando versiones anteriores de Qt...")
    subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y", "PyQt6", "PyQt6-WebEngine", "PyQt6-sip"], check=False)
    print("[*] Instalando dependencias...")
    print("[*] Instalando dependencias...")
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
    subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)

def create_spec_file():
    """Crear archivo .spec para PyInstaller"""
    print("[*] Creando archivo .spec...")

    spec_content = f"""# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['MarkdownViewer.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('README.md', '.'),
        ('LICENSE', '.'),
    ],
    hiddenimports=[
        'PySide6.QtCore',
        'PySide6.QtGui',
        'PySide6.QtWidgets',
        'PySide6.QtWebEngineWidgets',
        'PySide6.QtWebEngineCore',
        'markdown',
        'markdown.extensions.fenced_code',
        'markdown.extensions.tables',
        'markdown.extensions.toc',
        'markdown.extensions.nl2br',
        'markdown.extensions.sane_lists',
        'markdown.extensions.codehilite',
        'markdown.extensions.extra',
        'docx',
        'reportlab',
    ],
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=['PyQt6'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='{APP_NAME}',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
"""

    with open(f"{APP_NAME}.spec", "w") as f:
        f.write(spec_content)
    print(f"   Creado: {APP_NAME}.spec")

def build_executable():
    """Compilar ejecutable con PyInstaller"""
    print("[*] Compilando ejecutable...")

    cmd = [
        "pyinstaller",
        "--clean",
        f"{APP_NAME}.spec"
    ]

    result = subprocess.run(cmd)

    if result.returncode == 0:
        print("[OK] Ejecutable compilado exitosamente")
    else:
        print("[ERROR] Error al compilar ejecutable")
        sys.exit(1)

def create_windows_installer():
    """Crear instalador NSIS para Windows"""
    if platform.system() != "Windows":
        print("[WARN]  Instalador NSIS solo disponible en Windows")
        return

    print("[*] Creando instalador Windows NSIS...")

    nsis_script = f"""
!define APP_NAME "{APP_NAME}"
!define APP_VERSION "{VERSION}"
!define PUBLISHER "MarkdownViewer"
!define WEB_SITE "https://github.com/Yatrogenesis/MarkdownViewer"
!define APP_EXE "{APP_NAME}.exe"

!include "MUI2.nsh"

Name "${{APP_NAME}} ${{APP_VERSION}}"
OutFile "dist\\{APP_NAME}-{VERSION}-Windows-Setup.exe"
InstallDir "$PROGRAMFILES64\\${{APP_NAME}}"
InstallDirRegKey HKLM "Software\\${{APP_NAME}}" ""

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE "LICENSE"
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_LANGUAGE "English"

Section "MainSection" SEC01
    SetOutPath "$INSTDIR"
    File "dist\\${{APP_EXE}}"
    File "README.md"
    File "LICENSE"

    CreateDirectory "$SMPROGRAMS\\${{APP_NAME}}"
    CreateShortcut "$SMPROGRAMS\\${{APP_NAME}}\\${{APP_NAME}}.lnk" "$INSTDIR\\${{APP_EXE}}"
    CreateShortcut "$DESKTOP\\${{APP_NAME}}.lnk" "$INSTDIR\\${{APP_EXE}}"

    WriteRegStr HKLM "Software\\${{APP_NAME}}" "" "$INSTDIR"
    WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${{APP_NAME}}" "DisplayName" "${{APP_NAME}}"
    WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${{APP_NAME}}" "UninstallString" "$INSTDIR\\uninstall.exe"
    WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${{APP_NAME}}" "DisplayVersion" "${{APP_VERSION}}"
    WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${{APP_NAME}}" "Publisher" "${{PUBLISHER}}"

    WriteUninstaller "$INSTDIR\\uninstall.exe"
SectionEnd

Section "Uninstall"
    Delete "$INSTDIR\\${{APP_EXE}}"
    Delete "$INSTDIR\\README.md"
    Delete "$INSTDIR\\LICENSE"
    Delete "$INSTDIR\\uninstall.exe"

    Delete "$SMPROGRAMS\\${{APP_NAME}}\\${{APP_NAME}}.lnk"
    Delete "$DESKTOP\\${{APP_NAME}}.lnk"
    RMDir "$SMPROGRAMS\\${{APP_NAME}}"

    DeleteRegKey HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${{APP_NAME}}"
    DeleteRegKey HKLM "Software\\${{APP_NAME}}"

    RMDir "$INSTDIR"
SectionEnd
"""

    with open("installer.nsi", "w") as f:
        f.write(nsis_script)

    # Intentar compilar con NSIS si está instalado
    try:
        subprocess.run(["makensis", "installer.nsi"], check=True)
        print("[OK] Instalador Windows creado")
    except FileNotFoundError:
        print("[WARN]  NSIS no encontrado. Descarga desde: https://nsis.sourceforge.io/")

def create_linux_package():
    """Crear paquete .deb para Linux"""
    if platform.system() != "Linux":
        print("[WARN]  Paquete .deb solo disponible en Linux")
        return

    print("[*] Creando paquete .deb...")

    # Crear estructura de directorios
    pkg_dir = f"dist/{APP_NAME}-{VERSION}"
    os.makedirs(f"{pkg_dir}/DEBIAN", exist_ok=True)
    os.makedirs(f"{pkg_dir}/usr/bin", exist_ok=True)
    os.makedirs(f"{pkg_dir}/usr/share/applications", exist_ok=True)
    os.makedirs(f"{pkg_dir}/usr/share/doc/{APP_NAME}", exist_ok=True)

    # Archivo control
    control = f"""Package: {APP_NAME.lower()}
Version: {VERSION}
Section: editors
Priority: optional
Architecture: amd64
Maintainer: MarkdownViewer <noreply@github.com>
Description: Markdown Viewer & Editor
 Lightweight Markdown viewer and editor with PDF, DOCX, HTML export
"""
    with open(f"{pkg_dir}/DEBIAN/control", "w") as f:
        f.write(control)

    # Copiar ejecutable
    shutil.copy(f"dist/{APP_NAME}", f"{pkg_dir}/usr/bin/")
    os.chmod(f"{pkg_dir}/usr/bin/{APP_NAME}", 0o755)

    # Desktop entry
    desktop = f"""[Desktop Entry]
Type=Application
Name={APP_NAME}
Comment=Markdown Viewer & Editor
Exec=/usr/bin/{APP_NAME}
Terminal=false
Categories=Office;TextEditor;
"""
    with open(f"{pkg_dir}/usr/share/applications/{APP_NAME}.desktop", "w") as f:
        f.write(desktop)

    # Documentación
    shutil.copy("README.md", f"{pkg_dir}/usr/share/doc/{APP_NAME}/")
    shutil.copy("LICENSE", f"{pkg_dir}/usr/share/doc/{APP_NAME}/")

    # Construir paquete
    subprocess.run(["dpkg-deb", "--build", pkg_dir], check=True)
    print("[OK] Paquete .deb creado")

def create_macos_app():
    """Crear aplicación .app para macOS"""
    if platform.system() != "Darwin":
        print("[WARN]  Aplicación .app solo disponible en macOS")
        return

    print("[*] Creando aplicación macOS...")

    app_dir = f"dist/{APP_NAME}.app/Contents"
    os.makedirs(f"{app_dir}/MacOS", exist_ok=True)
    os.makedirs(f"{app_dir}/Resources", exist_ok=True)

    # Info.plist
    plist = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>{APP_NAME}</string>
    <key>CFBundleIdentifier</key>
    <string>com.github.yatrogenesis.markdownviewer</string>
    <key>CFBundleName</key>
    <string>{APP_NAME}</string>
    <key>CFBundleVersion</key>
    <string>{VERSION}</string>
    <key>CFBundleShortVersionString</key>
    <string>{VERSION}</string>
</dict>
</plist>
"""
    with open(f"{app_dir}/Info.plist", "w") as f:
        f.write(plist)

    # Copiar ejecutable
    shutil.copy(f"dist/{APP_NAME}", f"{app_dir}/MacOS/")
    os.chmod(f"{app_dir}/MacOS/{APP_NAME}", 0o755)

    # Crear DMG
    dmg_name = f"dist/{APP_NAME}-{VERSION}-macOS.dmg"
    subprocess.run([
        "hdiutil", "create", "-volname", APP_NAME,
        "-srcfolder", f"dist/{APP_NAME}.app",
        "-ov", "-format", "UDZO", dmg_name
    ], check=True)

    print("[OK] Aplicación macOS creada")

def create_portable_zip():
    """Crear versión portable en ZIP"""
    print("[*] Creando versión portable...")

    system = platform.system()
    arch = platform.machine()

    portable_dir = f"dist/{APP_NAME}-{VERSION}-{system}-{arch}-Portable"
    os.makedirs(portable_dir, exist_ok=True)

    # Copiar archivos
    exe_name = f"{APP_NAME}.exe" if system == "Windows" else APP_NAME
    shutil.copy(f"dist/{exe_name}", portable_dir)
    shutil.copy("README.md", portable_dir)
    shutil.copy("LICENSE", portable_dir)

    # Crear archivo ZIP
    shutil.make_archive(portable_dir, 'zip', portable_dir)
    shutil.rmtree(portable_dir)

    print(f"[OK] Versión portable creada: {portable_dir}.zip")

def main():
    """Función principal"""
    print(f"""
=========================================
  MarkdownViewer Build System v{VERSION}
=========================================
""")

    try:
        clean_build_dirs()
        install_dependencies()
        create_spec_file()
        build_executable()

        # Crear instaladores según plataforma
        system = platform.system()

        if system == "Windows":
            create_windows_installer()
        elif system == "Linux":
            create_linux_package()
        elif system == "Darwin":
            create_macos_app()

        create_portable_zip()

        print(f"""
======================================
  Build completado exitosamente
======================================

Archivos generados en dist/:
""")

        # Listar archivos generados
        for item in os.listdir("dist"):
            size = os.path.getsize(f"dist/{item}")
            size_mb = size / (1024 * 1024)
            print(f"  - {item} ({size_mb:.2f} MB)")

    except Exception as e:
        print(f"\n[ERROR] Error durante el build: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
