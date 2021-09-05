# 88ms 
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    result= []

    for value in intervals:
        if len(result)>0 and result[-1][1] >= value[0]:
            Max =result[-1][1]
            if value[1] > Max:
                result[-1][1] = value[1]

        else:
            result.append(value)
    return result
