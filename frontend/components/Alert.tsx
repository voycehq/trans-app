interface Props {
  children: any;
  className: "danger" | "success" | "warning" | "nothing";
  visible: boolean;
  rest?: any;
}

export default function Alert({
  children,
  className,
  visible = false,
  ...rest
}: Props) {
  const onClick = (event: any) => {
    event.currentTarget.classList.remove("danger");
    event.currentTarget.classList.remove("success");
    event.currentTarget.classList.remove("warning");
    event.currentTarget.style.visibility = "hidden";
    event.target.innerHTML = "";
  };
  return (
    <div
      // onClick={onClick}
      style={{ visibility: visible ? "visible" : "hidden", ...rest }}
      className={`alert ${className}`}
    >
      <p>{children}</p>
    </div>
  );
}
