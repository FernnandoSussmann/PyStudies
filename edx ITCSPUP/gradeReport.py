def gradeReport(course):
  #Assumes: course if of type grades
  report = []
  for s in course.allStudents():
    tot = 0.0
    numGrades = 0
    for g in course.getGrades(s):
      tot += g
      numGrades += 1
    try:
      avarege = tot/numGrades
      report.append(str(s) + '\'s mean grade is' + str(avarage))
    except ZeroDivisionError:
      report.append(str(s) + 'has no grades')
  return '\n'.join(report)
