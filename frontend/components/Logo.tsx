import Link from "next/link";

interface Props {
  to?: string;
}
const Logo = ({ to }: Props) => (
  <Link href={to ? to : "/"}>
    <a style={{ color: "black" }}>
      <h1>Voyce</h1>
    </a>
  </Link>
);

export default Logo;
