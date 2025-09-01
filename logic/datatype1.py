# def merge_dicts(d1:dict,d2:dict):
#     merged=d1.copy() # Start with keys and values of d1
#     for key,value in d2.items():
#         if key in merged:
#             merged[key]+=value
#         else:
#             merged[key]=value
#     return merged
# #give the input in the form of dictionaries
d1={"apple":10,"banana":5}
d2={"banana":3,"cherry":8}
# print(merge_dicts(d1,d2))
merged=(d1**d2)
print(merged)
