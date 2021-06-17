s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"
# \n \r \t \b \f \\
print(len(s1), len(s2), len(s3), len(s4), len(s5))
print("It's a good thing")
print('It is a "good" thing')
print("""It's a "good" thing""")

sql_query = """
select * 
from animals 
where common_name is 'wombat'
"""