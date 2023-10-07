export default function getListStudentIds(studentList) {
  let idList = [];
  if (studentList instanceof Array) {
    for (const student of studentList) {
      idList.push(student['id']);
    }
  }
  return idList;
}
