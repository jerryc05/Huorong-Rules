#!/usr/bin/env python3

import json
from pathlib import Path

with open(Path(__file__).parent / 'tencent-auto.json', 'rb+') as f:
    data = json.load(f)
    tencent = data['data']['*Tencent*']
    for x in tencent:
        allow_read = False
        for y in ('o', 't'):
            if Rf'\*.{y}tf' in x['res_path']:
                allow_read = True
        if x['res_path'] in (R'*\WinSXS\*', R'*\desktop.ini'):
            allow_read = True
        if allow_read:
            x['action_type'] = 2
            x['treatment'] = 0
    for p in [R'*\TPDownloadProxy', R'*\TPDownloadProxy\*', R'*\Intel\ShaderCache\*', R'*\AppData\Local\D3DSCache\*'] + [Rf'*\NVIDIA\{x}Cache\*' for x in ('DX', 'GL')]:
        tencent.append(
            {
                'res_path': p,
                'montype': 1,
                'action_type': 15,
                'treatment': 0,
            }
        )
    for p in (R'*\NormalColor\shellstyle.dll', R'*\chrome.exe', R'*\DCIM\*'):
        tencent.append(
            {
                'res_path': p,
                'montype': 1,
                'action_type': 2,
                'treatment': 0,
            }
        )
    for p in (R'*\Steam\*', R'*\RivaTuner Statistics Server\*', R'*\DiscordHook.dll'):
        tencent.append({'res_path': p, 'montype': 1, 'action_type': 15, 'treatment': 3})

    f.seek(0)
    f.truncate(0)
    f.write(json.dumps(data).encode('utf-8'))
