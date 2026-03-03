# 个人名片生成器
print("=" * 30)
print("    欢迎使用个人名片生成器")
print("=" * 30)

# 获取用户输入
name = input("请输入你的名字：")
job = input("请输入你的职业：")
hobby = input("请输入你的爱好：")

# 生成名片
print("\n" + "="*40)
print(f"【 个人名片 】")
print(f"姓名：{name}")
print(f"职业：{job}")
print(f"爱好：{hobby}")
print("="*40)
print("名片生成成功！🎉")
