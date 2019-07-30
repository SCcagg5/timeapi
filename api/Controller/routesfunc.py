from Model.basic import check
from Object.evts import evts

def dispo(cn, nextc):
    err = evts.disp()
    return cn.call_next(nextc, err)

def add(cn, nextc):
    err = check.contain(cn.pr, ["title", "desc", "location", "start", "end"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]
    err = evts.add(cn.pr["title"], cn.pr["desc"], cn.pr["location"], cn.pr["start"], cn.pr["end"])
    return cn.call_next(nextc, err)
