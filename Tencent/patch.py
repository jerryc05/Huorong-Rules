#!/usr/bin/env python3

import json
from pathlib import Path

with open(Path(__file__).parent / 'tencent-auto.json', 'rb+') as f:
    data = json.load(f)
    tencent = data['data']['*Tencent*']
    for x in tencent:
        allow_read = False
        for y in ('o', 't'):
            if f'*.{y}tf' in x['res_path']:
                allow_read = True
        if x['res_path'] == r'*\WinSXS\*':
            allow_read = True
        if allow_read:
            x['action_type'] = 2
            x['treatment'] = 0
    for x in ('DX', 'GL'):
        tencent.append(
            {
                'res_path': rf'*\NVIDIA\{x}Cache\*',
                'montype': 1,
                'action_type': 15,
                'treatment': 0,
            }
        )
    f.seek(0)
    f.truncate(0)
    f.write(json.dumps(data).encode('utf-8'))
