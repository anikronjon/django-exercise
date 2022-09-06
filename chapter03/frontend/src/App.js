import React, { useState, useEffect } from "react";
import axios from "axios";

const baseURL = "http://127.0.0.1:8000/api/posts/";

const App = () => {
  const [posts, setPosts] = useState(["hi"]);
  useEffect(() => {
    const posts = axios
      .get(baseURL)
      .then((response) => setPosts(response.data))
      .catch((error) => console.log(error));
  });

  return (
    <>
      <h2>React Frontend</h2>
      {posts.map((value, index) => {
        return 
        <>
            <h2>{value.id}</h2>
        </>;
      })}
    </>
  );
};

export default App;
