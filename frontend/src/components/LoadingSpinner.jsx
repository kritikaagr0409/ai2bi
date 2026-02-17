import { motion } from "framer-motion";

export default function LoadingSpinner() {
  return (
    <motion.div
      className="w-16 h-16 border-4 border-accent border-t-transparent rounded-full"
      animate={{ rotate: 360 }}
      transition={{ loop: Infinity, duration: 1 }}
    />
  );
}
