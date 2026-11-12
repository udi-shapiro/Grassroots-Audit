"""Run bounded probes and existing tests on the real pinned Dart runtime.

Run from the audit checkout root with arguments GLP_ROOT OUTPUT_DIRECTORY.
Every process has an OS-enforced timeout; a timeout is a recorded result,
not a successful test. This script never changes the remote GLP repository.
"""
from pathlib import Path
import json,shutil,subprocess,sys,time

source=Path(sys.argv[1]).resolve()
out=Path(sys.argv[2]).resolve();out.mkdir(parents=True,exist_ok=True)
cwd=source/'glp_runtime'
records=[]
def run(name,cmd,limit):
    start=time.monotonic()
    try:
        p=subprocess.run(cmd,cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=limit)
        result={'name':name,'command':cmd,'exit_code':p.returncode,'timeout':False,'seconds':round(time.monotonic()-start,3)}
        output=p.stdout
    except subprocess.TimeoutExpired as e:
        output=e.stdout or ''
        if isinstance(output,bytes):output=output.decode(errors='replace')
        result={'name':name,'command':cmd,'exit_code':None,'timeout':True,'seconds':round(time.monotonic()-start,3)}
    (out/(name+'.log')).write_text(output)
    records.append(result)
    (out/'runtime-results.json').write_text(json.dumps(records,indent=2)+'\n')
    print(json.dumps(result),flush=True)
    print(output[-12000:],flush=True)
    return result

run('dart-version',['dart','--version'],30)
run('disable-analytics',['dart','--disable-analytics'],30)
dependencies=run('pub-get',['dart','pub','get','--enforce-lockfile'],240)
if dependencies['exit_code']!=0:sys.exit(1)
shutil.copyfile(Path(__file__).with_name('runtime_probe.dart'),cwd/'_auditor_probe.dart')
for mode in ['typed_race_load','fifo_race']:
    run(mode,['dart','run','_auditor_probe.dart',mode],90)
print('Observations saved; inspect each exit code and test outcome before drawing conclusions.',flush=True)
