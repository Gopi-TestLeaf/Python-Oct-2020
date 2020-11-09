# Way1;
# import Learn_Modules.TestLeaf_Modules

# x = Learn_Modules.TestLeaf_Modules.TestLeaf01()
# x.python()
#
# y = Learn_Modules.TestLeaf_Modules.TestLeaf02()
# y.DevOps()
#
# Learn_Modules.TestLeaf_Modules.Basic_info()
# **********************************************************************************************************
# import Learn_Modules.TestLeaf_Modules as s
#
# x = s.TestLeaf01()
# x.python()
#
# y = s.TestLeaf02()
# y.DevOps()
#
# s.Basic_info()
# **********************************************************************************************************
# Way 2:
# from Learn_Modules.TestLeaf_Modules import TestLeaf01
# x = TestLeaf01()
# x.python()
# **********************************************************************************************************
# from Learn_Modules.TestLeaf_Modules import TestLeaf01 as x
# x.python()
# **********************************************************************************************************
# Way 3:
from Learn_Modules.TestLeaf_Modules import TestLeaf01, TestLeaf02, Basic_info
x = TestLeaf01()
y = TestLeaf02()
Basic_info()
# **********************************************************************************************************
from Learn_Modules.TestLeaf_Modules import TestLeaf01 as x, TestLeaf02 as y, Basic_info