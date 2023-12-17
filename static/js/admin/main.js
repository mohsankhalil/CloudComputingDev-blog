window.addEventListener("load", function () {
  let id_title = document.querySelector("#id_title");
  let id_slug = document.querySelector("#id_slug");

  id_title.addEventListener("change", (event) => {
    let slugvalue = id_title.value.replace(" ", "-").toLowerCase();
    id_slug.value = slugvalue;
  });
});
