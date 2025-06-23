# -*- mode: python ; coding: utf-8 -*-

block_cipher = None  # Removida a criptografia pois não está mais disponível

a = Analysis(
    ['painel.py'],
    pathex=[],  # Adicione caminhos adicionais se necessário, como ['D:\\Loader']
    binaries=[],
    datas=[
        ('Imagens', 'Imagens'),
        ('plant-logo-icon-design-free-vector.jpg', '.'),
        ('vector-soil-plant-icon (1).ico', '.'),
        ('main.py', '.'),
        ('keras_model.h5', '.'),
        ('labels.txt', '.'),
    ],
    hiddenimports=['customtkinter', 'tensorflow','opencv-python','matplotlib', 'PIL'],  # Corrigido 'Requests' para 'requests'
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],  # Removido 'runtime_hooks.py' (a menos que você tenha esse arquivo)
    excludes=[],
    noarchive=False,
    optimize=1,
    cipher=block_cipher,
)

# Configuração adicional para segurança (opcional)
# a.datas += [('licenca.key', 'path/to/your/license.key', 'DATA')]

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    name='main',
    debug=False,
    bootloader_ignore_signals=True,
    strip=True,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Se for GUI, mantenha como False
    disable_windowed_traceback=True,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='vector-soil-plant-icon (1).ico',  # Removido colchetes se apenas um ícone for usado
    aslr=True,
    dep=True,
)