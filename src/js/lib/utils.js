export function getCookie(c_name) {
  let st = "";
  let ed = "";
  if (document.cookie.length > 0) {
    st = document.cookie.indexOf(c_name + "=");
    if (st !== -1) {
      st = st + c_name.length + 1;
      ed = document.cookie.indexOf(";", st);
      if (ed === -1) ed = document.cookie.length;
      // 値をデコードして返す
      return unescape(document.cookie.substring(st, ed));
    }
  }
  return "";
}

export function generateFormData(obj) {
  return Object.keys(obj).reduce((o, key) => (o.set(key, obj[key]), o), new FormData());
}


export function getJson(url){
  return fetch(url, {
      method: 'GET',
      mode: 'same-origin',
      credentials: 'include',
      headers: {
        'X-CSRFToken': getCookie('csrftoken'),
        'Accept': 'application/json',
      },
    })
    .then(res => {
      return res.json();
    })
}

export function postJson(url, data, type='form'){
  let body = '';
  if (type === 'json'){
    body = JSON.stringify(data);
  }else{
    body = generateFormData(data);
  }
  return fetch(url, {
    method: 'POST',
    mode: 'same-origin',
    credentials: 'include',
    headers: {
      'X-CSRFToken': getCookie('csrftoken'),
      'Accept': 'application/json',
    },
    body: body,
  })
  .then(res => {
    return res.json();
  })
}