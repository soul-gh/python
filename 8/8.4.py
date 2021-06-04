#传递列表
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['alice','bob','dixi']
greet_users(usernames)

#函数中修改列表
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model:" + current_design)
    completed_models.append(current_design)
print("The following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
print("\n")

def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model:" + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("The following models have been printed:")
    for completed_model in completed_models:        
        print(completed_model)
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
print_models(unprinted_designs[:],completed_models)
show_completed_models(completed_models)
show_completed_models(unprinted_designs)