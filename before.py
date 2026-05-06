# 实验8：包含坏味道的示例代码
# 这个文件包含重复代码和过长函数的坏味道

def calculate_student_grade(students):
    """计算学生总分和等级（坏味道：逻辑冗余，未封装）"""
    result = []
    for student in students:
        # 坏味道：过长的逻辑块，缺乏封装
        total = student['math'] + student['english'] + student['science']
        if total >= 270:
            grade = "A"
        elif total >= 240:
            grade = "B"
        elif total >= 210:
            grade = "C"
        else:
            grade = "D"
        
        # 重复代码：此处有大量重复的打印逻辑（模拟坏味道）
        print(f"学生: {student['name']}")
        print(f"总分: {total}")
        print(f"等级: {grade}")
        print("--------------------")
        
        result.append({"name": student['name'], "total": total, "grade": grade})
    return result

def calculate_employee_bonus(employees):
    """计算员工奖金（坏味道：与上面函数高度相似，违反DRY原则）"""
    result = []
    for emp in employees:
        # 坏味道：重复的逻辑块（与calculate_student_grade几乎一样）
        salary = emp['base'] + emp['allowance']
        if salary >= 15000:
            bonus = salary * 0.2
        elif salary >= 10000:
            bonus = salary * 0.1
        else:
            bonus = salary * 0.05
        
        # 重复代码：打印逻辑完全一样
        print(f"员工: {emp['name']}")
        print(f"薪资: {salary}")
        print(f"奖金: {bonus}")
        print("--------------------")
        
        result.append({"name": emp['name'], "bonus": bonus})
    return result

# 未使用的变量（坏味道）
unused_variable = "This variable is never used"

# 测试数据
students = [
    {"name": "Alice", "math": 90, "english": 85, "science": 95},
    {"name": "Bob", "math": 70, "english": 65, "science": 80}
]

employees = [
    {"name": "John", "base": 12000, "allowance": 3000},
    {"name": "Jane", "base": 8000, "allowance": 2000}
]

# 执行函数
calculate_student_grade(students)
calculate_employee_bonus(employees)
