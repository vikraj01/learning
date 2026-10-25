import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import "@fontsource-variable/archivo/wdth.css";
import "@fontsource/jetbrains-mono/400.css";
import "@fontsource/jetbrains-mono/600.css";
import "@xterm/xterm/css/xterm.css";
import "./styles.css";
import Home from "./pages/Home";
import LabPage from "./pages/LabPage";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/lab/:id" element={<LabPage />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
