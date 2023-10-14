export default function updateStudentGradeByCity(studentList, city, newGrades) {
  return studentList
    .filter((student) => student.location === city)
    .map((student) => {
      const newGrade = newGrades.find((grade) => grade.studentId === student.id);
      if (newGrade) {
        return {
          ...student,
          grade: newGrade.grade
        };
      }
      return {
        ...student,
        grade: 'N/A',
      };
    });
}
