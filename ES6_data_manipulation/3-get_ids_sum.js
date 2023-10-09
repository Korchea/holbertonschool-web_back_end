export default function getStudentIdsSum(studentList) {
  const initialValue = 0;
  return studentList.reduce((accumulator, currentValue) => accumulator + currentValue.id, initialValue);
}
