# track_symbol_POC
track symbol with state.solver.get_variables() POC

BVS实例化时加入参数key=('var', 0)
需要求解时通过state.solver.get_variables('var')得到这些symbol

之前搞错了，每个state只会保存和自身相关的symbol，所以不用再通过state.solver.constraints.variables做对应，可以直接求解
        
运行结果：
```
[<Bool (KEY_41_32 & 0x1) != 0x0>, <Bool B_43_32 != 0x1>]
<BV32 KEY_41_32> eval to 1
<BV32 B_43_32> eval to fffffffe
---
[<Bool (KEY_41_32 & 0x1) == 0x0>, <Bool A_42_32 == 0x1>]
<BV32 KEY_41_32> eval to 0
<BV32 A_42_32> eval to 1
---
[<Bool (KEY_41_32 & 0x1) == 0x0>, <Bool A_42_32 != 0x1>]
<BV32 KEY_41_32> eval to 0
<BV32 A_42_32> eval to fffffffe
---
[<Bool (KEY_41_32 & 0x1) != 0x0>, <Bool B_43_32 == 0x1>]
<BV32 KEY_41_32> eval to 1
<BV32 B_43_32> eval to 1
```
