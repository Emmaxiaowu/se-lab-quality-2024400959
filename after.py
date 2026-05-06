# after.py - 重构：提取方法、消除重复、删除无用变量、单一职责
def filter_valid_scores(scores):
    """提取0-100的合法分数"""
    return [s for s in scores if 0 <= s <= 100]

def calculate_average(scores):
    """计算平均分"""
    valid_scores = filter_valid_scores(scores)
    return sum(valid_scores) / len(valid_scores) if valid_scores else 0

def is_pass(score):
    """判断是否及格"""
    return "及格" if score >= 60 else "不及格"

def print_student_report(name, scores):
    """打印学生成绩报告"""
    avg_score = calculate_average(scores)
    print(f"学生姓名: {name}")
    print(f"平均分: {avg_score}")
    print(f"结果: {is_pass(avg_score)}")

# 测试
scores = [85, 92, 78, 90]
print_student_report("张三", scores)
