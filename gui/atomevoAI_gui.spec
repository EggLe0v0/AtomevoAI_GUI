# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['atomevoAI_gui.py','module_gui.py',
               'C:\\Users\\le\\Desktop\\atomevoAI_GUI\\script\\aln2enc.py',
               'C:\\Users\\le\\Desktop\\atomevoAI_GUI\\script\\Bio_clustalw2.py',
               'C:\\Users\\le\\Desktop\\atomevoAI_GUI\\script\\csv2fasta.py',
               'C:\\Users\\le\\Desktop\\atomevoAI_GUI\\script\\explain.py',
               'C:\\Users\\le\\Desktop\\atomevoAI_GUI\\script\\fasta2csv.py',
               'C:\\Users\\le\\Desktop\\atomevoAI_GUI\\script\\modl.py',
               'C:\\Users\\le\\Desktop\\atomevoAI_GUI\\script\\predict.py',
               'C:\\Users\\le\\Desktop\\atomevoAI_GUI\\script\\train.py'],
             pathex=[],
             binaries=[],
             datas=[('xgboost', 'xgboost'), ('shap', 'shap')],
             hiddenimports=['PySide', 'gtk',
                            'sklearn.neighbors._typedefs',
                            'sklearn.utils._typedefs',
                            'sklearn.neighbors._partition_nodes',
                            'sklearn',
                            'xgboost',
                            'numpy'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='atomevoAI_gui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
