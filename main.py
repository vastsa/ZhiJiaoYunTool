print("【欢迎使用职教云综合助手】")
print("                  By:Lan")
print("【0】职教云签到监控功能")
print("【1】职教云签到改命功能")
game = int(input("请选择功能："))
if game == 0:
    from autoqiandao import main
    main()
elif game == 1:
    from buqiao import menu
    menu()
