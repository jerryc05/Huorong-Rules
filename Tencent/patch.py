#!/usr/bin/env python3

import json
import sys

with open(sys.argv[1], 'rb+') as f:
    data = json.load(f)
    tencent = data['data']['*Tencent*']
    for x in tencent:
        for y in ('o', 't'):
            if rf'\\*.{y}tf' in x['res_path']:
                x['action_type'] = 2
                x['treatment'] = 0
    for x in ('common-controls', 'gdiplus'):
        tencent.append(
            {
                "res_path": rf"*\WinSXS\x86_microsoft.windows.{x}*",
                "montype": 1,
                "action_type": 2,
                "treatment": 0,
            }
        )
    f.seek(0)
    f.truncate(0)
    f.write(json.dumps(data).encode('utf-8'))
