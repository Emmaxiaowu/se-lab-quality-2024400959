# 实验8：重构后的代码
# 修复了重复代码和过长函数的问题

def print_record(name, info1_label, info1_value, info2_label, info2_value):
    """提取公共打印逻辑（消除重复代码）"""
    print(f"姓名: {name}")
    print(f"{info1_label}: {info1_value}")
    print(f"{info2_label}: {info2_value}")
    print("--------------------")

def calculate_student_grade(students):
    """计算学生总分和等级（重构后）"""
    result = []
    for student in students:
        total = student['math'] + student['english'] + student['science']
        grade = get_grade(total) # 提取方法
        
        # 调用公共打印方法
        print_record(student['name'], "总分", total, "等级", grade)
        
        result.append({"name": student['name'], "total": total, "grade": grade})
    return result

def get_grade(score):
    """提取评分逻辑（消除过长函数）"""
    if score >= 270:
        return "A"
    elif score >= 240:
        return "B"
    elif score >= 210:
        return "C"
    else:
        return "D"

def calculate_employee_bonus(employees):
    """计算员工奖金（重构后）"""
    result = []
    for emp in employees:
        salary = emp['base'] + emp['allowance']
        bonus_rate = get_bonus_rate(salary) # 提取方法
        bonus = salary * bonus_rate
        
        # 调用公共打印方法
        print_record(emp['name'], "薪资", salary, "奖金", bonus)
        
        result.append({"name": emp['name'], "bonus": bonus})
    return result

def get_bonus_rate(salary):
    """提取奖金比例逻辑"""
    if salary >= 15000:
        return 0.2
    elif salary >= 10000:
        return 0.1
    else:
        return 0.05

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
