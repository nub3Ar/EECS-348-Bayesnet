def ask(var, value, evidence, bn):
	hypo_dict = dict(evidence)
	hypo_dict[var] = value
	print(hypo_dict)
	hypo_dict_f = dict(evidence)
	hypo_dict_f[var] = not value
	print(hypo_dict)
	a = ask_recurse(list(bn.variables),hypo_dict, bn)
	b = ask_recurse(list(bn.variables),hypo_dict_f, bn)
	print(a, b)
	return(a/(a+b))

def ask_recurse(vars, values, bn):
	#recursion is done when no more variables in the list
	if (len(vars) == 0):
		return 1
	var = vars.pop(0)
	if var.name in list(values):
		prob = var.probability(values[var.name], values)
		return prob * ask_recurse(vars,values,bn)
	else:
		values_t = dict(values)
		values_t[var.name] = True
		values_f = dict(values)
		values_f[var.name] = False
		var_t = list(vars)
		var_f = list(vars)
		return (var.probability(True, values)*ask_recurse(var_t, values_t, bn)+var.probability(False, values)*ask_recurse(var_f, values_f, bn))
