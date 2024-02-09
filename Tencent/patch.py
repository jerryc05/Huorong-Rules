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
    
    for x in tencent:
        if x['res_path'] == "*\\CryptnetUrlCache\\*":
            x['action_type'] = 12
            x['treatment'] = 3
            break

    tencent.append({
        "res_path": R"*\Windows\*",
        "montype": 1,
        "action_type": 13,
        "treatment": 3
    })
    tencent.append({
        "res_path": R"*\Windows\*",
        "montype": 1,
        "action_type": 2,
    })

    for p in [R'*\TPDownloadProxy', R'*\TPDownloadProxy\*', R'*\Intel\ShaderCache\*', R'*\AppData\Local\D3DSCache\*', R'*\qq_guild\*',  R'*\WXWork\*', R'*\WXDrive\*', R'*\wxworkweb\*', R'*\ProgramData\boost_interprocess\*'] + [Rf'*\{x}Cache\*' for x in ('DX', 'GL')]:
        tencent.append(
            {
                'res_path': p,
                'montype': 1,
                'action_type': 15,
                'treatment': 0,
            }
        )
    # allow read
    for p in (R'*\NormalColor\shellstyle.dll', R'*\chrome.exe', R'*\DCIM\*', f"{Path.home()/'Desktop'}\\*", R'*\Accessibility.api', R'*AdobeAAMDetect32.dll'):
        tencent.append(
            {
                'res_path': p,
                'montype': 1,
                'action_type': 2,
                'treatment': 0,
            }
        )
    # all deny
    for p in (R'*\Steam\*', R'*\RivaTuner Statistics Server\*', R'*\DiscordHook.dll', R'*\xfolder\*'):
        tencent.append({'res_path': p, 'montype': 1, 'action_type': 15, 'treatment': 3})

    f.seek(0)
    f.truncate(0)
    f.write(json.dumps(data).encode('utf-8'))
