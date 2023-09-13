export default function createReportObject(employeesList) {
  return {
    allEmployees: employeesList,
    getNumberOfDepartments: Object.keys(allEmployees).length,
  };
}