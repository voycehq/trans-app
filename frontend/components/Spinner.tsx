import styles from "../styles/components/Spinner.module.sass";

interface Props {
  visible: boolean;
  size?: number;
  bgColor?: string;
}

function Spinner({
  visible,
  bgColor,
  size = 20,
  ...rest
}: Props): JSX.Element | null {
  if (!visible) return null;
  const width = (size / 16).toString() + "rem";

  return (
    <div className={styles.spinner} style={{ ...rest }}>
      <div
        className={styles.loader}
        style={{
          borderLeftColor: bgColor,
          height: width,
          width,
        }}
      ></div>
    </div>
  );
}

export default Spinner;
