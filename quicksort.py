q=lambda i:(q([x for x in i[1:]if x<i[0]])+[i[0]]+q([x for x in i[1:]if x>=i[0]]))if i else[]
