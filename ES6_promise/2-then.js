export default function handleResponseFromAPI(promise) {
  try {
    return promise.resolve({ status: 200, body: 'Success' }); // when successful
  } catch {
    return Error();  // when error
  } finally {
    console.log('Got a response from the API');
  };
}
