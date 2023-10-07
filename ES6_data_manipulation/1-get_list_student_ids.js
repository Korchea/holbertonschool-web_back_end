export default function getListStudentIds(studentList) {
  if (studentList instanceof Array) {
    const idList = studentList.map(student => student['id']);
    return idList;
  } else {
    return [];
  }
}
