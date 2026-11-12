import re
def declaration(path,name):
    text=re.sub(r'%[^\n]*','',path.read_text())
    text=text[re.search(r'^'+re.escape(name)+r'\(',text,re.M).start():]
    pattern=r"\s*(('[^']*')|([A-Za-z_][A-Za-z_0-9]*)|([0-9]+)|([(),\[\].=]))"
    tokens=[];pos=0
    while pos<len(text):
        m=re.match(pattern,text[pos:])
        if not m:
            assert not text[pos:].strip(),text[pos:pos+80]
            break
        tokens.append(m.group(1));pos+=m.end()
    at=0
    def take(expected=None):
        nonlocal at
        t=tokens[at];at+=1
        if expected is not None:assert t==expected,(t,expected)
        return t
    def term():
        t=take()
        if t=='[':
            a=[]
            if tokens[at]!=']':
                a.append(term())
                while tokens[at]==',':take(',');a.append(term())
            take(']');v=tuple(a)
        else:
            v=t.strip("'")
            if tokens[at]=='(':
                take('(');a=[term()]
                while tokens[at]==',':take(',');a.append(term())
                take(')');v=(v,*a)
        if tokens[at]=='=':take('=');v=('=',v,term())
        return v
    value=term();take('.')
    return value

