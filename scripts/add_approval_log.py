#!/usr/bin/env python3
import argparse
from pathlib import Path
from datetime import datetime

p = argparse.ArgumentParser()
p.add_argument('--request-id', required=True)
p.add_argument('--requester', required=True)
p.add_argument('--action-type', required=True)
p.add_argument('--amount', default='0')
p.add_argument('--decision', required=True)
p.add_argument('--approver', required=True)
p.add_argument('--notes', default='')
a = p.parse_args()

log = Path('docs/logs/approval-log.md')
entry = f"""- Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}
  - Request ID: {a.request_id}
  - Requester: {a.requester}
  - Action Type: {a.action_type}
  - Amount (JPY): {a.amount}
  - Decision: {a.decision}
  - Approver: {a.approver}
  - Notes: {a.notes}

"""
text = log.read_text() if log.exists() else '# Approval Log\n\n'
log.write_text(text + entry)
print('[OK] appended approval log')
