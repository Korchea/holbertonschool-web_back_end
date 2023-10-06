export default function getFullResponseFromAPI(success) {
  const myPromise = new Promise((myResolve, myReject) => {
    if (success === true) {
      myResolve({ status: 200, body: 'Success' });
    } else {
      myReject(Error('The fake API is not working currently'));
    }
  });
  return myPromise;
}
