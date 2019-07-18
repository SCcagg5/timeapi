calendar_data = []

class calendar:
    def disp(start, end):
        ret = []

        for i in calendar_data:
            if int(i["end"]) >= start or int(i["start"]) <= end:
                ret.append(i)
        return [True, {"res": ret}, 200]

    def reserve(start, end, desc):
        for i in calendar_data:
            if int(i["start"]) <= start and int(i["end"]) >= start:
                return [False, "", 403]
            if int(i["start"]) <= end and int(i["end"]) >= end:
                return [False, "", 403]
        calendar_data.append({"start": start, "end": end, "desc": desc})
        return [True, {"start": start, "end": end, "desc": desc}, 200]
