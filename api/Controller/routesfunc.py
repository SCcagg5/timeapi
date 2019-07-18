from Model.basic import check
from Object.calendar import calendar

def reserve(cn, nextc):
    err = check.contain(cn.pr, ["start", "end", "desc"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]

    err = calendar.reserve(cn.pr["start"], cn.pr["end"], cn.pr["desc"])
    return cn.call_next(nextc, err)

def dispo(cn, nextc):
    err = check.contain(cn.pr, ["start", "end"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]

    err = calendar.disp(cn.pr["start"], cn.pr["end"])
    return cn.call_next(nextc, err)
