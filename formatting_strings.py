from string import Template
the_str="The quick brown $animal $action over the lazy dog"
the_template=Template(the_str)
output_str=the_template.substitute(animal="fox",action="jumped")
print(output_str)
args={
    "animal":"cow",
    "action":"walked"
}
output_str = the_template.substitute(args)
print(output_str)
foo="foo"
bar=123
print("output:{},{}".format(foo,bar))
print("output:{1},{0}".format(foo,bar))
print("output:{var1},{var2}".format(var1=foo,var2=bar))
print("output:{var1},{var2:x},{var2:X}".format(var1=foo,var2=bar))
product="Widget"
price=19.99
tax=0.07
