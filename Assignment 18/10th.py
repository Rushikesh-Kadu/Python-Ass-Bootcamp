sample_dict = {'C': 92,'Java': 66,'Python': 85}
value=sorted(sample_dict.values())[0]
for x in sample_dict:
    if sample_dict[x]==value:
        print(x,":",sample_dict[x])
        break

