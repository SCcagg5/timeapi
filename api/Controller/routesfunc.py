from Model.basic import check
from Object.evts import evts

def dispo(cn, nextc):
    err = check.contain(cn.pr, ["mail"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    err = evts.disp(cn.private["creds"])
    return cn.call_next(nextc, err)

def add(cn, nextc):
    err = check.contain(cn.pr, ["title", "desc", "location", "start", "end"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]
    err = evts.add(cn.pr["title"], cn.pr["desc"], cn.pr["location"], cn.pr["start"], cn.pr["end"], cn.private["creds"])
    return cn.call_next(nextc, err)

def creds(cn, nextc):
    err = check.contain(cn.pr, ["mail"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]
    err = evts.getcred(cn.pr["mail"])
    cn.private["creds"] = err[1]
    return cn.call_next(nextc, err)
