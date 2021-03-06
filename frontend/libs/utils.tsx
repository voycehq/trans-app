export const colors = {
  primary_color: "#012b65",
  second_color: "#005399",
  white_color: "#fff",
  text_color: "#70757a",
  black_color: "#000",
  hover_color: "#f8f8f8",
  icon_color: "#64676c",
  grey: "rgba(0, 0, 0, 0.1)",
  border: "1px solid #dadce0",
};

export const http =
  process.env.NODE_ENV === "production"
    ? "https://api.voyce.rimscloud.co"
    : "http://localhost:4000";
