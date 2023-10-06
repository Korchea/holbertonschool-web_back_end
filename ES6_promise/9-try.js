export default function guardrail(mathFunction) {
  let funRet = '';
  try {
    funRet = mathFunction();
  } catch (err) {
    funRet = err.toString();
  }
  const queue = [funRet, 'Guardrail was processed'];
  return queue;
}
